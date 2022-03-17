from googleapiclient.discovery import build
import config
import util
import argparse
import os

youtube = build('youtube', 'v3', developerKey=os.environ['API_KEY'])


def get_channel_videos(channel_id):
    """Fetch the list of videos present under the channel id.
    
    :param channel_id: youtube channel id of the user
    :return : list of videos
    
    """
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos


def get_videos_stats(video_id):
    """Fetch the statistics corresponding to the provided video id. 
    
    :param video_id : youtube video id
    :return stats: statistics of video
    """
    stats = []
    for i in range(0, len(video_id)):
        res = youtube.videos().list(id=video_id[i],
                                    part='statistics').execute()
        stats += res['items']

    return stats


def video_table(list_of_videos):
    """Fetch the list of videos present under the channel id.
    
    :param channel_id: youtube channel id of the user
    :return : list of videos
    """
    for video in list_of_videos:
        config.channel_id.append(video['snippet']['channelId'])
        config.channel_name.append(video['snippet']['channelTitle'])
        config.video_id.append(video['snippet']['resourceId']['videoId'])
        config.video_type.append(video['snippet']['resourceId']['kind'])
        config.video_title.append(video['snippet']['title'])
        config.video_description.append(video['snippet']['description'])
        config.publishedAt.append(video['snippet']['publishedAt'])


def stat_table(video_stats):
    """Joins all the required columns.
    
    :param video_stats : list of videos 
    :return : no value 
    """
    for stat in video_stats:
        if util.key_in_dict_and_not_none(stat['statistics'], "viewCount"):
            config.view_count.append(stat['statistics']['viewCount'])
        else:
            config.view_count.append(0)
        if util.key_in_dict_and_not_none(stat['statistics'], "likeCount"):
            config.like_count.append(stat['statistics']['likeCount'])
        else:
            config.like_count.append(0)
        if util.key_in_dict_and_not_none(stat['statistics'], "dislikeCount"):
            config.dislike_count.append(stat['statistics']['dislikeCount'])
        else:
            config.dislike_count.append(0)
        if util.key_in_dict_and_not_none(stat['statistics'], "favoriteCount"):
            config.favoriteCount.append(stat['statistics']['favoriteCount'])
        else:
            config.favoriteCount.append(0)
        if util.key_in_dict_and_not_none(stat['statistics'], "commentCount"):
            config.commentCount.append(stat['statistics']['commentCount'])
        else:
            config.commentCount.append(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output_dir",
        type=str,
    )

    parser.add_argument(
        "--channel_id",
        type=str
    )

    args = parser.parse_args()

    list_of_videos = get_channel_videos(args.channel_id)
    video_table(list_of_videos)
    video_stats = get_videos_stats(config.video_id)
    stat_table(video_stats)
    util.write_output(zip(config.channel_id, config.channel_name,
                          config.video_id, config.video_type, config.video_title,
                          config.video_description, config.view_count, config.like_count,
                          config.dislike_count, config.favoriteCount, config.commentCount,
                          config.publishedAt),
                      config.channel_name[0],
                      args.output_dir)
