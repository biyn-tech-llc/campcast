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
    ('Moses and Associates', 'C50_'),
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
    ('Ready At 20', 'C98_'),
    ('Let My People Go', 'C99_'),
    ('Victory In Laodecia', 'C100_', '1503520278_VICTORY%20IN%20LAODICEA.jpg'),
    ('Stir It Up', 'C101_'),
    ('Where Is The Flock That Was Given Thee?', 'C102_', 'where%20is%20the%20flock%3f.jpg'),
    ('A Super Mega Church', 'C103_'),
    ('I Will Multiply Them And They Shall Not Be Few', 'C104_', 'I%20WILL%20MULTIPLY.jpg'),
    ('Army of Hard Followers', 'C105_'),
    ('A Small One Shall Become A Strong Nation', 'C106_', '1544740349_a%20small%20one%20shall%20become%20a%20strong%20nation.jpg'),
    ('Reasons For The Breakup', 'C107_'),
    ('Arise And Shine', 'C108_'),
    ('Obligations Of Christian Workers', 'C109_'), 
    ('The Church Must Send Or It Will End', 'C110_'),
    ('No City Shall Be Too Strong For You', 'C111_'),
    ('Neutralize The Curse', 'C112_', 'neutralise.jpg'),
    ('Zealously Affected', 'C113_'),
    #('', ''), #114 seems to be an incomplete collection
    ('Everything By Prayer Nothing Without Prayer', 'C115_', 'Everything%20by%20Prayer%20Nothing%20without%20Prayer.jpg', '2017-08-24'),
    ('Labour To Be Blessed', 'C115_', 'labour%20to%20be%20blessed.jpg', '2017-10-24'),
    ('Make Yourself a Saviour of Men', 'C116_'),
    ('The Reward For Hard Work Is More Work', 'C117_', 'the%20reward%20for%20hard.jpg'),
    ('No Weeping No Gnashing', 'C118_'),
    ('Candle In The Dark', 'C119_'),
    ('Twenty-Five To Fifty', 'C120_'),
    ('The Isles Shall Wait For Me', 'C121_'),
    ('Attempt Great Things For God', 'C122_'),
    ('And Ye Shall Compass The City', 'C123_', 'and%20ye%20shall.jpg', '2018-10-31.05'),
    ('No City Shall Be Too Strong For You 2018', 'C123_', 'no%20city%20shall%20be%20too%20strong%20for%20you.jpg', '2018-10-31.07'),
    #('Life In The Church', 'C124_'), #repeat of C19_
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

<head>
  <meta charset="utf-8">
  <title>CampCast</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="style/inline.css">

  <link rel="manifest" href="manifest.xml">
</head>

<body>

<!-- Header -->
<header class="header">
  <h1 class="header__title">Camp Cast</h1>
  <p>Click on a camp thumbnail picture to copy its RSS feed. Then paste RSS feed into your podcast application to subscribe.</p>
  <p>Most podcast players subscribe to RSS feed directly - including iTunes podcast, Podcast Addict, etc. <i>Google Play Music and Google Podcasts do not.</i></p>
  <p><a href="https://medium.com/@joshmuccio/how-to-manually-add-a-rss-feed-to-your-podcast-app-on-desktop-ios-android-478d197a3770">This article has help</a> for adding RSS links to many podcast apps.</p>
</header>

<!-- Photo Grid -->
<div class="row"> 
'''

list_page_footer = '''
</div>

<script src="methods.js"></script>

</body>
</html>
'''
column_h = '''  <div class="column">
'''
column_f = '''  </div>
'''

fig = '''
    <figure data-toggle="tooltip" onclick="copyTextToClipboard('___PODCASTRSS___', '___CAMPID___')" onmouseout="mouseOut('___CAMPID___')">
      <img class=scaled src="___IMAGE___" style="width:100%">
      <figcaption>___TITLE___</figcaption>
    </figure>
'''
max_cols = 8
col_len = len(camps) / max_cols + (1 if len(camps) % max_cols else 0)
list_page = list_page_header
camp_number = 1
for camp in camps:
    name = camp[0]
    expr = camp[1]
    expr2 = '' if len(camp) < 4 else (camp[3] + '.*')

    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*mp3\)\".*" + expr2 + "$/\\1/p allsongs.html" 
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
    folder = name.lower().replace(' ', '_').replace("'","").replace('?', '')
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
