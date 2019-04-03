#!/usr/bin/python

import subprocess
import os
import re
import requests

camps = [
    ('Building a Multiple Mega Church', 'C1_'),
    ('Loyalty and the Mega Church', 'C2_'),
    ('Strive Lawfully For A Mega Church',   'C3_'),
    ('Double Mega Missionary Church',       'C4_'),
    ('Going Deeper and Doing More', 'C5_'),
    ('Love and The Mega Church', 'C6_'),
    ('The Dream Church', 'C7_'),
    ('Advancing in Pergamos', 'C10_'),
    ('Work of the ministry', 'C11_'),
    ('Pastors of Thousands', 'C12_'),
    ('The Message of Sacrifice', 'C13_'),
    ('Victory in Laodicea', 'C14_'),
    ('What Is Your Life', 'C15_'),
    ('All Out', 'C16_'),
    ('Allos - Another of the Kind', 'C17_', 'allos.jpg'),
    ('Grace n peace', 'C18_'),
    ('Life In The Church', 'C19_'),
    ('The Mega Church', 'C20_'),
    ('The Mysteries Of God', 'C21_'),
    ('Zogreo', 'C22_'),
    ('Agree on the Way', 'C23_'),
    ('HOW TO SURVIVE IN EPHESUS', 'C24_'),
    ('The Presence', 'C25_'),
    ('Kruptos Man', 'C26_'),
    ('Gates and Roads', 'C27_'),
    ('Bema', 'C28_'),
    ('Victory In Pergamos', 'C29_'),
    ('Barrenness and Fruitfulness', 'C30_'),
    ('Preparation of The Gospel', 'C31_'),
    ('MISSIONS AND MISSIONARIES', 'C32_'),
    ('OTHERS', 'C32_'),
    ('church planting', 'C34_'),
    ('Perfection', 'C35_'),
    ('Snake Junction', 'C36_'),
    ('Australia 1000', 'C37_'),
    ('Take Up Your Cross', 'C38_'),
    ('Birthday - Kee Waa', 'C39_', 'BIRTHDAY%20(KEEWAA).jpg'),
    ('Busselization', 'C40_', 'BUSSELISATION.jpg'),
    ('Obedience Unto Death', 'C41_'),
    ('Become Who You Can Become', 'C42_'),
    ('Spiritual Battles', 'C43_'),
    ('Apocalypse', 'C44_'),
    ("The Lord's Anointed", 'C45_'),
    ('Do The Work Of An Evangelist', 'C46_'),
    ('I and My Children', 'C47_', 'I%20AND%20THE%20CHILDREN.jpg'),
    ('Missions', 'C48_'),
    ('The Calling', 'C50_'),
    ('Tell Them', 'C51_'),
    ('The Sufferings of Christ', 'C52_'),
    ('The Powers of a Cross', 'C53_', '1504183776_POWERS%20OF%20A%20CROSS.jpg'),
    ('Warfare Keys', 'C55_'),
    ('Finish What You Started', 'C56_'),
    ('Mighty Foundations', 'C57_'),
    ('My First Love', 'C58_'),
    ('Coming Out of Obscurity', 'C59_'),
    ('Lay Power', 'C60_'),
    ('The Blessings of Abraham', 'C61_', 'THE%20BLESSING%20OF%20ABRAHAM.jpg'),
    ('Predestination', 'C62_'),
    ('Why You Are Not a Missionary', 'C63_', 'WHY%20ARE%20YOU%20NOT%20A%20MISSIONARY.jpg'),
    ('Tasters or Partakers', 'C64_', 'Tasters%20&amp;%20Partakers.jpg'),
    ('The Privilege', 'C65_', 'The%20Priviledge.jpg'),
    ('The Bag of Seeds', 'C66_'),
    ('If You Love The Lord', 'C67_'),
    ('That my house may be filled', 'C68_'),
    ('Warnings of purpose', 'C69_'),
    ('The Volante', 'C70_'),
    ('Awake O Sleeper', 'C71_'),
    ('Lord I know you need somebody', 'C72_'),
    ('Inexorability in the Mission', 'C73_'),
    ("God's Banquet", 'C74_'),
    ('Many Are Called', 'C75_'),
    ('The Word of my Patience', 'C76_'),
    ('Be thou faithful unto death', 'C77_'),
    ('The Sweet influences of The Holy Spirit', 'C78_', 'sweet%20influences.jpg'),
    ('Secrets of the Anointing and His Anointing', 'C79_', '1544765559_the%20secret.jpg'),
    ('Atmosphere', 'C80_', 'atmosphere.jpg'),
    ('One Hundred Million Souls', 'C81_', '100-Million-Souls.jpg'),
    ('The beautiful Job', 'C82_'),
    ('Principles of war', 'C83_'),
    ('Fight The Good Fight', 'C84_'),
    ('Wise As Serpents', 'C85_'),
    ('Give Thyself Wholly', 'C86_', 'give%20thyself%20.jpg'),
    ("Mission America 'There must be Missions'", 'C87_', 'mission%20america.jpg'),
    ('Mission Europe', 'C88_', 'MISSION%20EUROPE.jpg'),
    ("Mission SA 'Prepare the way of the Lord'", 'C89_', 'mission%20south%20africa.jpg'),
    ("Mission Africa 'The ministry of the sower'", 'C90_', '1498920239_Mission-Africa-Dag-Heward-Mills.jpg'),
    ('Who is he that overcomes the world', 'C91_'),
    ('God Requireth That Which Is Past', 'C92_'),
    ('How Can I Say Thanks', 'C93_'),
    ('Fulfil Your Ministry', 'C94_'),
    ('Obligation of Christians', 'C95_', 'Obligation%20_of_Christians.jpg'),
    ('Attempt Great Things', 'C96_'),
    ('Expect Great Things', 'C97_'),
    ('Controlling The Flesh', 'C98_'),
    ('Let My People Go', 'C99_'),
    ('Victory In Laodecia', 'C100_', '1503520278_VICTORY%20IN%20LAODICEA.jpg'),
    ('You Are Supernatural', 'C101_'),
    ('Where Is The Flock That Was Given Thee?', 'C102_', 'where%20is%20the%20flock%3f.jpg'),
    ('Why We Must Have A Mega Church', 'C103_'),
    ('The Destiny of the Church', 'C104_'),
    ('Army of Hard Followers', 'C105_'),
    ('Bearing Fruit', 'C106_'),
    ('Reasons For The Breakup', 'C107_'),
    ('Arise And Shine', 'C108_'),
    #('', ''), #109 seems to be an incomplete compilation
    ('The Church Must Send Or It Will End', 'C110_'),
    ('No City Shall Be Too Strong For You', 'C111_'),
    ('Neutralize The Curse', 'C112_', 'neutralise.jpg'),
    ('The Mystery of Our Marriage to God', 'C113_'),
    #('', ''), #114 seems to be an incomplete collection
    ('Everything By Prayer Nothing Without Prayer', 'C115_'),
    ('Make Yourself a Saviour of Men', 'C116_'),
    ('The Reward For Hard Work Is More Work', 'C117_', 'the%20reward%20for%20hard.jpg'),
    ('No Weeping No Gnashing', 'C118_'),
    ('Candle In The Dark', 'C119_'),
    ('Twenty-Five To Fifty', 'C120_'),
    ('The Isles Shall Wait For Me', 'C121_'),
    ('Attempt Great Things For God', 'C122_'),
    ('Life In The Church', 'C124_'),
]
FILES_URL="http://daghewardmillsaudio.org/songs/"
LINK_URL="https://biyn-tech-llc.github.io/campcast/"
IMAGES_URL="http://daghewardmillsaudio.org/images/albums/"
episode = '''
    <item>
      <title>___EPISODE___</title>
      <description>___EPISODE___</description>
      <pubDate>Tue, 26 Mar 2019 12:00:00 GMT</pubDate>
      <enclosure url="___URL___"
                 type="audio/mpeg"/>
      <!--itunes:duration>30:00</itunes:duration-->
      <guid isPermaLink="false">___URL___</guid>
    </item>
'''
pod_header = '''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:googleplay="http://www.google.com/schemas/play-podcasts/1.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">
  <channel>
    <title>___TITLE___</title>
    <googleplay:author>Bishop Dag Heward-Mills</googleplay:author>
    <description>___TITLE___</description>
    <googleplay:image href="___IMAGE___"/>
    <language>en-us</language>
    <link>___LINK___/</link>
    <image>
        <url>
            ___IMAGE___
        </url>
        <width>192</width>
        <height>144</height>
    </image>
'''

pod_footer = '''
  </channel>
</rss>
'''

pod_page = '''
<html>
  <head>
    <link rel="alternate" type="application/rss+xml" title="Podcast"
          href="___PODCASTRSS___"/>
    <title>___TITLE___</title>
  </head>
  <body>
    <h1>Machaneh Love!</h1>
  </body>
</html>
'''

list_page_header = '''
<!DOCTYPE html>
<html>
<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: Arial;
}

.header {
  text-align: center;
  padding: 32px;
}

.row {
  display: -ms-flexbox; /* IE10 */
  display: flex;
  -ms-flex-wrap: wrap; /* IE10 */
  flex-wrap: wrap;
  padding: 0 0px;
}

/* Create four equal columns that sits next to each other */
.column {
  -ms-flex: 25%; /* IE10 */
  flex: 25%;
  max-width: 25%;
  padding: 0 0px;
}

.column img {
  margin-top: 0px;
  vertical-align: middle;
}

/* Responsive layout - makes a two column-layout instead of four columns */
@media screen and (max-width: 800px) {
  .column {
    -ms-flex: 50%;
    flex: 50%;
    max-width: 50%;
  }
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
    -ms-flex: 100%;
    flex: 100%;
    max-width: 100%;
  }
}

figure {
  text-align: center;
  font-style: italic;
  font-size: smaller;
  text-indent: 0;
  border: thin silver solid;
  margin: 0em;
  padding: 0.1em;
  width: 100%;
}
img.scaled {
  width: 100%;
}

.tooltip {
  position: relative;
  display: inline-block;
}

.tooltip .tooltiptext {
  visibility: hidden;
  width: 140px;
  background-color: #555;
  color: #fff;
  text-align: center;
  border-radius: 6px;
  padding: 5px;
  position: absolute;
  z-index: 1;
  bottom: 75%;
  left: 50%;
  margin-left: -75px;
  opacity: 0;
  transition: opacity 0.3s;
}

.tooltip .tooltiptext::after {
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: #555 transparent transparent transparent;
}

.tooltip:hover .tooltiptext {
  visibility: visible;
  opacity: 1;
}

</style>
<body>

<!-- Header -->
<div class="header">
  <h1>The Camps below may be played with your podcast app - <i>if it accepts RSS feeds directly</i></h1>
  <p>Click on a camp to copy its RSS feed into the clipboard. Then paste the link into your podcast application.</p>
  <p>Most podcast players have this feature - including iTunes podcast, Podcast Addict, etc. <i>Google Play Music and Google Podcasts do not.</i></p>
  <p><a href="https://medium.com/@joshmuccio/how-to-manually-add-a-rss-feed-to-your-podcast-app-on-desktop-ios-android-478d197a3770">This article has help</a> for adding RSS links to many podcast apps.</p>
</div>

<!-- Photo Grid -->
<div class="row"> 
'''

list_page_footer = '''
</div>

<script>
function fallbackCopyTextToClipboard(text) {
  var textArea = document.createElement("textarea");
  textArea.value = text;
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Fallback: Copying text command was ' + msg);
  } catch (err) {
    console.error('Fallback: Oops, unable to copy', err);
  }

  document.body.removeChild(textArea);
}
function copyTextToClipboard(text, element_id) {
  var tooltip = document.getElementById(element_id);
  tooltip.innerHtml = "Copied: " + text;
  
  if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text);
    return;
  }
  navigator.clipboard.writeText(text).then(function() {
    console.log('Async: Copying to clipboard was successful!');
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });
}

function mouseOut(element_id) {
  var tooltip = document.getElementById(element_id)
  tooltip.innerHtml = "Click image to copy RSS feed to clipboard"
}
</script>

</body>
</html>
'''
column_h = '''  <div class="column">
'''
column_f = '''  </div>
'''

fig = '''
    <figure class="tooltip" onclick="copyTextToClipboard('___PODCASTRSS___', '___CAMPID___')" onmouseout="mouseOut('___CAMPID___')">
      <span class="tooltiptext" id="___CAMPID___">Click image to copy RSS feed to clipboard</span>
      <img class=scaled src="___IMAGE___" style="width:100%">
      <figcaption>___TITLE___</figcaption>
    </figure>
'''
max_cols = 4
col_len = len(camps) / max_cols + (1 if len(camps) % max_cols else 0)
list_page = list_page_header
camp_number = 1
for camp in camps:
    name = camp[0]
    expr = camp[1]
    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*mp3\)\".*$/\\1/p allsongs.html" 
    #print cmd
    ssns = subprocess.check_output(cmd.split())
    #print "sessions are: " + ssns
    image = LINK_URL + 'DAG.jpg'
    if len(camp) >= 3:
        image = IMAGES_URL + camp[2]
    else:
        cmd = "grep -i -m 1 " + name.replace(' ', '.*') + " images.html"
        try:
            image_line = subprocess.check_output(cmd.split())
            image_file = re.search(r'(?<=href=").*jpg(?=">)', image_line).group(0)
            image = IMAGES_URL + image_file
            #print image
            if requests.get(image).status_code != 200:
                image = LINK_URL + 'DAG.jpg'
        except subprocess.CalledProcessError, e:
            print str(e) 

    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*jpg\).*$/\\1/p allsongs.html" 
    folder = name.lower().replace(' ', '_').replace("'","")
    podcast = pod_header.replace('___TITLE___', name) \
                .replace('___LINK___', LINK_URL + folder) \
                .replace('___IMAGE___', image)
    for ssn in ssns.split():
        #print FILES_URL + ssn
        ssnTitle = ssn.split('.mp3')[0].split(expr)[1].replace('%20', ' ')
        epis = episode.replace('___URL___', FILES_URL + ssn).replace('___EPISODE___', ssnTitle)
        #print epis
        podcast += epis

    podcast += pod_footer
    #print podcast
    pod_dir = os.path.join(folder, 'rss')
    if not os.path.exists(pod_dir):
        os.makedirs(pod_dir)
    podfile = os.path.join(pod_dir, "podcast.rss")
    #print podfile 
    with open(os.path.join(pod_dir, "podcast.rss"), "w") as rss_file:
        rss_file.write(podcast)
    with open(os.path.join(folder, 'index.html'), 'w') as html_file:
        html_file.write(pod_page.replace('___PODCASTRSS___', LINK_URL + podfile) \
            .replace('___TITLE___', name))
    
    # column opening tag
    if (camp_number % col_len) == 1:
        list_page += column_h

    # the podcast entry
    list_page += fig.replace('___PODCASTRSS___', LINK_URL + podfile) \
            .replace('___TITLE___', name) \
            .replace('___IMAGE___', image) \
            .replace('___CAMPID___', folder)

    # column closing tag
    if ((camp_number % col_len) == 0 or camp_number == len(camps)):
        list_page += column_f

    camp_number += 1

list_page += list_page_footer 
with open ("index.html", "w") as top_html:
    top_html.write(list_page)
