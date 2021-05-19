#/bin/bash
#
# Create timelapse of images with today's date

cd /media/pi/SeagateExternal/timelapse_images

/usr/bin/rm timelapse-wip.mp4

#
# Today's dated timelapse
#

fd=$(/usr/bin/date +"%Y%m%d")

/usr/bin/ffmpeg -r 24 -pattern_type glob -i "original/image-${fd}-*.jpg" -s hd1080 -vcodec libx264 timelapse-wip.mp4

mv timelapse-wip.mp4 "timelapse-${fd}.mp4"

#
# Cumulative timelapse
#

#/usr/bin/ffmpeg -r 24 -pattern_type glob -i "image-*.jpg" -s hd1080 -vcodec libx264 timelapse-wip.mp4
#
#mv timelapse-wip.mp4 timelapse.mp4

