#!/usr/bin/python

import subprocess
import os

camps = [
    ('Strive Lawfully For A Mega Church',   'C3_'),
    ('Double Mega Missionary Church',       'C4_')
]
FILES_URL="http://daghewardmillsaudio.org/songs/"
LINK_URL="https://biyn-tech-llc.github.io/campcast/"
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
        <width>144</width>
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
    cmd = "sed -ne s/^.*href=\"\(" + expr + ".*mp3\).*$/\\1/p allsongs.html" 
    #print cmd
    ssns = subprocess.check_output(cmd.split())
    #print ssns
    folder = name.lower().replace(' ', '_')
    podcast = pod_header.replace('___TITLE___', name) \
                .replace('___LINK___', LINK_URL + folder) \
                .replace('___IMAGE___', LINK_URL + 'DAG.jpg')
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
    print podfile 
    with open(os.path.join(pod_dir, "podcast.rss"), "w") as rss_file:
        rss_file.write(podcast)
    with open(os.path.join(folder, 'index.html'), 'w') as html_file:
        html_file.write(pod_page.replace('___PODCASTRSS___', LINK_URL + folder + '/index.html') \
            .replace('___TITLE___', name))

