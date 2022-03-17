# ChannelStats

A command line utility to fetch the channel stats of a youtube channel.

# Installation instruction
After cloning this repository.

``` 
git clone  https://github.com/Ravineesh/YouTubeGrabber.git 
cd YouTubeGrabber/src 
pip install -r requirements.txt
```

Before running the `channel_stats.py` you have export the `API_KEY` via tha command line. `API_KEY` key can be generated from your Youtube Developer account.
```
 $export  API_KEY='your_api_key'
```

Run the following command.

 `` python channel_stats.py --output_dir '/home/' --channel_id XXXXX  ``
 
 The parameters required:
- `--channel_id` : Youtube channel id.
- `--output_dir`: The path of csv file which contains channel statistics
 
Output csv file will contain the following fields

| Command | Description |
| --- | --- |
| channel_id | channel id of user |
| channel_name | name of channel |
| video_id | video id |
| type | you video or youtube shorts |
| video_title | video title |
| video_description | video description |
| view_count | total views |
| like_count | total likes |
| dislike_count | dislike counts |
| favoriteCount | favorite counts |
| commentCount | number of comments |
| publishedAt | date and time of upload |