from instaloader import Instaloader, Profile

# Initialize Instaloader
L = Instaloader()

username = "zia_linc_insta_py"
password = "Uni.linc.1997"

# Load session from file if it exists, otherwise log in
try:
    L.load_session_from_file(username, "session-file")
    print("Session loaded successfully.")
except FileNotFoundError:
    print("Session file not found. Logging in...")
    L.login(username,password )
    L.save_session_to_file("session-file")
    print("Session saved to file.")

# URL of the Instagram post
insta_post_url = input('Enter the Instagram post URL: ')

# Extract shortcode from URL
shortcode = insta_post_url.split('/')[-2]  # Fetch the post id
print(f'Short code: {shortcode}\n')

# Download post
post = instaloader.Post.from_shortcode(L.context, shortcode)
if post.is_video:
    print(f"Downloading video from {post.url}")
    L.download_post(post, target='insta_downloads')
else:
    print("The specified post does not contain a video.")
