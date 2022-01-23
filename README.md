# Dynamic_Ad_Insertion_For_Live
Step 1:
Create API in flask:
https://your-host/dash/start_stream?content_id=12345
{
	"status": "streaming started"
}
Background process:
1. In this method dash-sample-video url should call and get xml data, url liks http://streaming.com/match/dash/index.mpd
2. Manipulating the XML by replacing base URL. http://streaming.com/match/
This process should happened every 3 seconds in background. Local file should updated with new XML content in every 3 seconds.

Steps 2:
- Local XML should insert with ads in another method

https://your-host/dash/get_stream?content_id=12345&user_id=abcd, parent method.
- Local XML should respond by inserting ads, is's child.
