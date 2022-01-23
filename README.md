# Dynamic_Ad_Insertion_For_Live
Read Streaming Data from here : https://demo.daiconnect.com/live/dash/usp/dash_blue/.mpd?requestuid=bbd47347-840b-44e3-bb47-2d3bd57b7d6b
In background process in which interval the file will update
https://demo.daiconnect.com/live/dash/usp/dash_blue/.mpd?requestuid=bbd47347-840b-44e3-bb47-2d3bd57b7d6b
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


Basic guides

Step 1:
API:
API, to start stream.
After hitting API, background process need to initiate.

Background process:
- Need to get data from https://demo.daiconnect.com/live/dash/usp/dash_blue/.mpd?requestuid=bbd47347-840b-44e3-bb47-2d3bd57b7d6b URL
- Keep it in variable, and manipulating it by replacing base URL
- XML content after manipulating need to store in local xml file for first time, from second hit the local file need to update with real time content.
- Fetching from URL then write in local xml by manipulating shuold process in every 3 seconds.





https://docs.aws.amazon.com/mediatailor/
http://streaming.com/match/dash/index.mpd
https://github.com/aminyazdanpanah/python-ffmpeg-video-streaming
https://docs.aws.amazon.com/mediatailor/latest/ug/manifest-dash.html
https://docs.aws.amazon.com/mediatailor/latest/ug/dash-manifest-time-signal-example.html
https://docs.aws.amazon.com/mediatailor/latest/ug/single-period-dash-manifest-example.html *
https://docs.aws.amazon.com/mediatailor/latest/ug/dash-manifest-splice-insert-example.html
