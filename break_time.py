import webbrowser, time, random

for _ in range(3):
	time.sleep(60*60)
	l = ["https://youtu.be/4uTNVumfm84","https://youtu.be/09R8_2nJtjg", "https://www.youtube.com/watch?v=e-ORhEE9VVg", "https://www.youtube.com/watch?v=nfs8NYg7yQM", "https://www.youtube.com/watch?v=lp-EO5I60KA"]
	webbrowser.open(random.choice(l))