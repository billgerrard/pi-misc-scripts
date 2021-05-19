#/bin/bash
#
# Overlay date timestamp on images 

if [ -z "$1" ]
then
    # default to today
    #
    fd=$(/usr/bin/date +"%Y%m%d")
else
    fd=$1
fi

echo "Generating timestamp overlays for $fd"

cd /media/pi/SeagateExternal/timelapse_images/original

DATE=$fd
FILES="${DATE}/image-${DATE}-*.jpg"

###image-20210202-*.jpg

mkdir -p ../overlay/${DATE}

for f in $FILES
do
  img_name=`echo $f | rev | cut -d'/' -f-1 | rev`
  #echo $img_name

  src_file="original/${DATE}/${img_name}"
  dst_file="overlay/${DATE}/overlay-${img_name}"
  ovr_date=$(/usr/bin/date -r $f +"%Y-%m-%d %I:%M%P")

  echo "Processing ${src_file} -> ${dst_file} [${ovr_date}]"

  $(/usr/bin/convert $f -pointsize 50 -fill white -gravity southwest -annotate +70+50 "$ovr_date" "../${dst_file}")

done
