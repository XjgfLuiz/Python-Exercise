text = input("file name: ").lower().strip()

if text.endswith(".gif"):
    print("image/gif")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".pdf"):
    print("application/pdf")
elif text.endswith(".mp3"):
    print("audio/mp3")
elif text.endswith(".mp4"):
    print("video/mp4")
else:
    print("application/octet-stream")