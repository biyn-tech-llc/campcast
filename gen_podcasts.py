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
    ('Grace n peace', 'C18_'),
    ('Life In The Church', 'C19_'),
    ('The Mega Church', 'C20_'),
    ('The Mystries Of God', 'C21_'),
    ('Zogreo', 'C22_'),
    ('Agree on the Way', 'C23_'),
    ('HOW TO SURVIVE IN EPHESUS', 'C24_'),
    ('The Presence', 'C25_'),
    ('Kruptos Man', 'C26_'),
    ('Gates and Roads', 'C27_'),
    ('Victory In Pergamos', 'C29_'),
    ('Barrenness and Fruitfulness', 'C30_'),
    ('Preparation of The Gospel', 'C31_'),
    ('MISSIONS AND MISSIONARIES', 'C32_'),
    ('OTHERS', 'C32_'),
    ('church planting', 'C34_'),
    ('Perfection', 'C35_'),
    ('Busselization', 'C40_'),
    ('Obedience Unto Death', 'C41_'),
    ('Apocalypse', 'C44_'),
    ("The Lord's Anointed", 'C45_'),
    ('Do The Work Of An Evangelist', 'C46_'),
    ('I and My Children', 'C47_'),
    ('Missions', 'C48_'),
    ('Tell Them', 'C51_'),
    ('The Sufferings of Christ', 'C52_'),
    ('The Powers of a Cross', 'C53_'),
    ('Warfare Keys', 'C55_'),
    ('Finish What You Started', 'C56_'),
    ('Mighty Foundations', 'C57_'),
    ('My First Love', 'C58_'),
    ('Lay Power', 'C60_'),
    ('The Blessings of Abraham', 'C61_'),
    ('Predestination', 'C62_'),
    ('Why You Are Not a Missionary', 'C63_'),
    ('Tasters or Partakers', 'C64_'),
    ('Privilage', 'C65_'),
    ('The Bag of Seeds', 'C66_'),
    ('If You Love The Lord', 'C67_'),
    ('That my house may be filled', 'C68_'),
    ('Warnings of purpose', 'C69_'),
    ('The Volante', 'C70_'),
    ('Awake O Sleeper', 'C71_'),
    ('Lord I know you need somebody', 'C72_'),
    ('Inexorability in the Mission', 'C73_'),
    ("God's Banquet", 'C74_'),
    ('The Word of my Patience', 'C76_'),
    ('Be thou faithful unto death', 'C77_'),
    ('The Sweet influences of The Holy Spirit', 'C78_'),
    ('Secrets of the Anointing and His Anointing', 'C79_'),
    ('The beautiful Job', 'C82_'),
    ('Principles of war', 'C83_'),
    ("Mission America 'There must be Missions'", 'C87_'),
    ('Mission Europe', 'C88_'),
    ("Mission SA 'Prepare the way of the Lord'", 'C89_'),
    ("Mission Africa 'The ministry of the sower'", 'C90_'),
    ('Who is he that overcomes the world', 'C91_')
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
      <itunes:duration>30:00</itunes:duration>
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

for camp in camps:
    name = camp[0]
    expr = camp[1]
    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*mp3\)\".*$/\\1/p allsongs.html" 
    #print cmd
    ssns = subprocess.check_output(cmd.split())
    #print "sessions are: " + ssns
    cmd = "grep -i " + name.replace(' ', '.*') + " images.html"
    image = LINK_URL + 'DAG.jpg'
    try:
        image_line = subprocess.check_output(cmd.split())
        image_file = re.search(r'(?<=href=").*jpg', image_line).group(0)
        image = IMAGES_URL + image_file
        #print image
        if requests.get(image).status_code != 200:
            image = LINK_URL + 'DAG.jpg'
    except subprocess.CalledProcessError, e:
        print str(e) 

    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*jpg\).*$/\\1/p allsongs.html" 
    folder = name.lower().replace(' ', '_')
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
        html_file.write(pod_page.replace('___PODCASTRSS___', LINK_URL + folder + '/index.html') \
            .replace('___TITLE___', name))

