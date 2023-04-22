timestamp=`date '+%Y-%m-%d-%H-%M-%S'`
echo time stamp is ${timestamp}
mkdir -p backups

mv -f allsongs.html backups/allsongs-${timestamp}.html
curl -ks "https://www.daghewardmillsaudio.org/songs/" -o allsongs.html

mv -f images.html backups/images-${timestamp}.html
curl -ks http://daghewardmillsaudio.org/images/albums/ -o images.html