for i in $( seq 1000 1427 ) ; do
    j="2022-04-02-19-29-07_frame0"$i
    #echo "frame0"$i.jpg $j.jpg
    mv "frame"$i.jpg $j.jpg
done 
