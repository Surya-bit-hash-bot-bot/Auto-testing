@Client.on_message(filters.private & (filters.document | filters.video | filters.audio))
async def auto_rename_files(client, message):    
    user_id = message.from_user.id

    format_template = await AshutoshGoswami24.get_format_template(user_id)
    media_preference = await AshutoshGoswami24.get_media_preference(user_id)

    if not format_template:
        return await message.reply_text("Please set an auto-rename format first using /autorename")

    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        media_type = media_preference or "document"
    elif message.video:
        file_id = message.video.file_id
        file_name = f"{message.video.file_name}.mp4"
        media_type = media_preference or "video"
    elif message.audio:
        file_id = message.audio.file_id
        file_name = f"{message.audio.file_name}.mp3"
        media_type = media_preference or "audio"
    else:
        return await message.reply_text("Unsupported File Type")

    print(f"Original File Name: {file_name}")

    # Check whether the file is already being renamed or has been renamed recently
    if file_id in renaming_operations:
        elapsed_time = (datetime.now() - renaming_operations[file_id]).seconds
        if elapsed_time < 10:
            print("File is being ignored as it is currently being renamed or was renamed recently.")
            return

    # Mark the file as currently being renamed
    renaming_operations[file_id] = datetime.now()

    # Extract episode number and qualities
    episode_number = extract_episode_number(file_name)
    print(f"Extracted Episode Number: {episode_number}")

    if episode_number:
        placeholders = ["episode", "Episode", "EPISODE", "{episode}"]
        for placeholder in placeholders:
            format_template = format_template.replace(placeholder, str(episode_number), 1)

        quality_placeholders = ["quality", "Quality", "QUALITY", "{quality}"]
        for quality_placeholder in quality_placeholders:
            if quality_placeholder in format_template:
                extracted_qualities = extract_quality(file_name)
                if extracted_qualities == "Unknown":
                    await message.reply_text("I Was Not Able To Extract The Quality Properly. Renaming As 'Unknown'...")
                    del renaming_operations[file_id]
                    return
                format_template = format_template.replace(quality_placeholder, "".join(extracted_qualities))   

        if not os.path.isdir("Metadata"):
            os.mkdir("Metadata")

        _, file_extension = os.path.splitext(file_name)
        new_file_name = f"{format_template}{file_extension}"
        file_path = f"downloads/{new_file_name}"

        file = message
        download_msg = await message.reply_text(text="Trying To Download.....")
        try:
            path = await client.download_media(message=file, file_name=file_path, progress=progress_for_pyrogram, progress_args=("Download Started....", download_msg, time.time()))
        except Exception as e:
            del renaming_operations[file_id]
            return await download_msg.edit(e)  

        _bool_metadata = await AshutoshGoswami24.get_metadata(message.chat.id)  

        if (_bool_metadata):
            metadata_path = f"Metadata/{new_file_name}"
            metadata = await AshutoshGoswami24.get_metadata_code(message.chat.id)
            if metadata:
                await download_msg.edit("I Found Your Metadata🔥\n\n__Please Wait...__\n`Adding Metadata ⚡...`")
                cmd = f"""ffmpeg -i "{path}" {metadata} "{metadata_path}" """
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                if er:
                    return await download_msg.edit(str(er) + "\n\n**Error**")
            await download_msg.edit("**Metadata Added To The File Successfully ✅**\n\n__**Please Wait...**__\n\n`😈Trying To Downloading`")
        else:
            await download_msg.edit("`😈Trying To Downloading`") 

        duration = 0
        try:
            metadata = extractMetadata(createParser(file_path))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
        except Exception as e:
            print(f"Error getting duration: {e}")

        upload_msg = await download_msg.edit("Trying To Uploading⚡.....")
        ph_path = None 
        c_caption = await AshutoshGoswami24.get_caption(message.chat.id)
        c_thumb = await AshutoshGoswami24.get_thumbnail(message.chat.id)

        caption = c_caption.format(filename=new_file_name, filesize=humanbytes(message.document.file_size), duration=convert(duration)) if c_caption else f"**{new_file_name}**"

        if c_thumb:
            ph_path = await client.download_media(c_thumb)
            print(f"Thumbnail downloaded successfully. Path: {ph_path}")
        elif media_type == "video" and message.video.thumbs:
            ph_path = await client.download_media(message.video.thumbs[0].file_id)

        if ph_path:
            Image.open(ph_path).convert("RGB").save(ph_path)
            img = Image.open(ph_path)
            img.resize((320, 320))
            img.save(ph_path, "JPEG")    

        try:
            if media_type == "document":
                await client.send_document(
                    message.chat.id,
                    document=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started.....", upload_msg, time.time())
                )
                await client.send_document(
                    Config.DUMP_CHANNEL,
                    document=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=f"**{new_file_name}**\nUploaded by {message.from_user.mention()}"
                )
            elif media_type == "video":
                await client.send_video(
                    message.chat.id,
                    video=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started.....", upload_msg, time.time())
                )
                await client.send_video(
                    Config.DUMP_CHANNEL,
                    video=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=f"**{new_file_name}**\nUploaded by {message.from_user.mention()}"
                )
            elif media_type == "audio":
                await client.send_audio(
                    message.chat.id,
                    audio=metadata_path if _bool_metadata else file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=("Upload Started.....", upload_msg, time.time())
                )
                await client.send_audio(
                    Config.DUMP_CHANNEL,
                    audio=metadata_path if _bool_metadata else file_path,
                    thumb=ph_path,
                    caption=f"**{new_file_name}**\nUploaded by {message.from_user.mention()}"
                )
        except Exception as e:
            os.remove(file_path)
            if ph_path:
                os.remove(ph_path)
            if metadata_path:
                os.remove(metadata_path)
            return await upload_msg.edit(f"Error: {e}")

        await download_msg.delete() 
        if ph_path:
            os.remove(ph_path)
        if file_path:
            os.remove(file_path)
        if metadata_path:
            os.remove(metadata_path)
                
