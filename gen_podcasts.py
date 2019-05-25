#!/usr/bin/python

import subprocess
import os
import re
import requests
import time
from PIL import Image
from io import BytesIO


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
    ('Seigneur Ait Pitie', 'C75_'),
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
    ('Season of Withdrawal','X','1550854868_season%20of%20withdrawal.jpg','','X1.%20Prophets%20or%20Spirituals.mp3 \
                                                                              X2.%20Prophets%20or%20Spirituals_Prayer%20Session.mp3 \
                                                                              X3.%20The%20Fall%20of%20Lucifer.mp3 \
                                                                              X4.%20The%20Fall%20of%20Lucifer_Prayer%20Session%20.mp3 \
                                                                              X5.%20Dialogue%20or%20Monologue.mp3 \
                                                                              X6.%20Dialogue%20or%20Monologue_Prayer%20Session.mp3 \
                                                                              X7.%20What%20Prayer%20Births.mp3 \
                                                                              X8.%20Coveting%20The%20Best%20and%20Super%20Abounding%20.mp3 \
                                                                              X9.%20Coveting%20The%20Best%20and%20Super%20Abounding_Prayer%20Session.mp3 \
                                                                              X10.%20The%20Fall%20of%20Lucifer.mp3 \
                                                                              X11.%20The%20Mistake%20of%20Not%20Obeying.mp3 \
                                                                              X12.%20The%20Mistake%20of%20Not%20Obeying_Prayer%20Session.mp3 \
                                                                              X13.%20The%20Need%20to%20Resist%20DIsobedience%20.mp3 \
                                                                              X14.%20The%20Need%20to%20Resist%20DIsobedience_Prayer%20Session%20.mp3 \
                                                                              X15.%20Compassing%20the%20City.mp3 \
                                                                              X16.%20Compassing%20the%20City_Prayer%20Session.mp3 \
                                                                              X17.%20Follow%20the%20Ark%20(The%20Anointing).mp3 \
                                                                              X18.%20Follow%20the%20Ark%20(The%20Anointing)_Prayer%20Session.mp3 \
                                                                              X19.%20Learning%20to%20Pray%20Longer.mp3 \
                                                                              X20.%20Testimonies%20and%20Sharing%20.mp3 \
                                                                              X21.%20Territory%20Taking%20Prayers%20with%20Bishop%20Ogoe.mp3 \
                                                                              X22.%20Demonic%20Powers%20You\'re%20Overcoming.mp3 \
                                                                              X23.%20Demonic%20Powers%20You\'re%20Overcoming_Prayer%20Session.mp3 \
                                                                              X24.%20Lead%20us%20not%20into%20Temptation%20.mp3 \
                                                                              X25.%20Pleading%20the%20Blood.mp3 \
                                                                              X26.%20Not%20My%20Will,%20but%20Thy%20will%20be%20done.mp3 \
                                                                              X27.%20Not%20My%20will,%20but%20Thy%20will%20be%20done_Prayer%20Session.mp3 \
                                                                              X28.%20Prayers%20with%20Rev%20Frank.mp3 \
                                                                              X29.%20Prayers%20with%20Rev%20Frank.mp3 \
                                                                              X30.%20The%20Great%20Deception.mp3 \
                                                                              X31.%20The%20Great%20Deception_Prayer%20Session.mp3 \
                                                                              X32.%20No%20Turning%20Back%20from%20Your%20Calling.mp3 \
                                                                              X33.%20No%20Turning%20back%20from%20your%20Calling_Prayer%20Session.mp3 \
                                                                              X34.%20Thanks%20Giving%20for%20a%20Net%20Full%20of%20Fishes.mp3 \
                                                                              X35.%20The%20Mysteries%20of%20His%20Will.mp3 \
                                                                              X36.%20The%20Mysteries%20of%20His%20Will_Prayer%20Session.mp3 \
                                                                              X37.%20The%20Mysteries%20of%20His%20Will_Prayer%20Session%20Pt.%202.mp3 \
                                                                              X38.%20His%20Mysterious%20Will%20Starts%20Immediately.mp3 \
                                                                              X39.%20His%20Mysterious%20Will%20Starts%20Immediately_Prayer%20Session.mp3 \
                                                                              X40.%20Awake%20O%20Sleeper.mp3'),
]
FILES_URL="http://daghewardmillsaudio.org/songs/"
LINK_URL="https://www.machanehcast.com/"
IMAGES_URL="http://daghewardmillsaudio.org/images/albums/"
episode = '''
    <item>
      <title>___EPISODE___</title>
      <description>___EPISODE___</description>
      <pubDate>Tue, 26 Mar 2019 12:___TRACKORDER___ GMT</pubDate>
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
  <title>MachanehCast</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="style/inline.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

  <link rel="apple-touch-icon" sizes="57x57" href="apple-icon-57x57.png">
  <link rel="apple-touch-icon" sizes="60x60" href="apple-icon-60x60.png">
  <link rel="apple-touch-icon" sizes="72x72" href="apple-icon-72x72.png">
  <link rel="apple-touch-icon" sizes="76x76" href="apple-icon-76x76.png">
  <link rel="apple-touch-icon" sizes="114x114" href="apple-icon-114x114.png">
  <link rel="apple-touch-icon" sizes="120x120" href="apple-icon-120x120.png">
  <link rel="apple-touch-icon" sizes="144x144" href="apple-icon-144x144.png">
  <link rel="apple-touch-icon" sizes="152x152" href="apple-icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180" href="apple-icon-180x180.png">
  <link rel="icon" type="image/png" sizes="192x192"  href="android-icon-192x192.png">
  <link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="96x96" href="favicon-96x96.png">
  <link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
  <link rel="manifest" href="manifest.json">
  <meta name="msapplication-TileColor" content="#ffffff">
  <meta name="msapplication-TileImage" content="ms-icon-144x144.png">
  <meta name="theme-color" content="#ffffff">

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

  <script src="enjoyhint/enjoyhint.min.js"></script>
  <link href="enjoyhint/enjoyhint.css" rel="stylesheet">
  <style>
  .enjoy_hint_label {
      text-align:left;
  }
  </style>

  <link rel="stylesheet" type="text/css" href="style/help.css">

</head>

<body>

<div class="navibar">
  <a href="#" class="icon" id="idhelp" onclick="openNav()">
    <i class="fa fa-bars"></i>
  </a>
  <span id=idthis>The Machaneh Directory</span>
  <input type="search" placeholder="Search.." id="idsearch" oninput="campSearch()"/>
</div>

<!-- Photo Grid -->
<div class="imgrow" id="allcamps"> 
'''

list_page_footer = '''
</div>


<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <span>How to use Podcast Directory</span>
  <button class="accordion">Usage</button>
  <div class="panel">
    <ul><li>Tap or click on a podcast thumbnail picture - its RSS link is copied.</li>
    <li>Subscribe to the camp's podcast in your podcast app. See below for help.</li> 
    <li>To find a particular camp, scroll down for more thumbnails, or use the search bar at the top right.</li></ul>
  </div>
  <span>Adding podcast by URL link</span>
  <button class="accordion">Podcasts (iOS)</button>
  <div class="panel">
    <ol><li>Launch Podcasts app.</li>
    <li>Go to Library if you are not there already.</li>
    <li>Tap on Edit.</li>
    <li>Select Add a Podcast by URL.</li></ol>
  </div>
  <button class="accordion">Podcast Addict (Android)</button>
  <div class="panel">
    <ol>
      <li>Launch app and go to main screen</li>
      <li>Press the <i class="fa fa-plus-circle fa-fw"></i> to add a new podcast.</li>
      <li>Press the icon labeled RSS - the first on the top row.</li>
      <li>The RSS link should be already pasted. Verify and press <i>ADD</i> button at bottom.</li>
    </ol>
  </div>
  <button class="accordion">Podbean (Android)</button>
  <div class="panel">
    <ol>
      <li>Launch app and go to main screen.</li>
      <li>Click on the <i class="fa fa-search fa-fw"></i> icon.</li>
      <li>Hide the keyboard when it pops up to reveal the <i>Add Feed URL</i> button. Tap the button.</li>
      <li>Clear the http:// from the input box and long press to paste the Feed URL.</li>
      <li>Tap the <i>Done</i> button at top right. </li>
      <li>Tap the <i>Follow</i> button to add to followed podcasts.</li>
    </ol>
  </div>
  <button class="accordion">Overcast (iOS)</button>
  <div class="panel">
    <ol>
      <li>Tap the + button in the top right like you normally would to add a podcast.</li>
      <li>Then tap <i>Add URL</i> in the top right.</li>
      <li>Paste the feed URL and hit done!</li>
    </ol>
  </div>
  <button class="accordion">Downcast (iOS)</button>
  <div class="panel">
    <ol>
      <li>Tap <i>Add</i> on the bottom bar.</li>
      <li>Press <i>Add Podcast Manually</i> and in the <i>Feed</i> field.</li>
      <li>Paste the URL of the RSS feed.</li>
      <li>Hit <i>Subscribe</i> in the top right.</li>
    </ol>
  </div>
  <button class="accordion">Pocket Casts (iOS, Android & Web)</button>
  <div class="panel">
    <ol>
      <li>Paste the URL of the feed into the search field and hit search. Done!</li>
    </ol>
  </div>
  <button class="accordion">Podcast App Not Listed?</button>
  <div class="panel">
    <p>If your podcast app is not covered here, you may search for instructions on the internet, or in the app's help pages.</p>
    <p>Some podcast apps do not allow subscribing with URL - namely Soundcloud, Google Play, Google Podcasts, Spotify, iHearRadio, etc.</p>
  </div>
</div>

<script src="methods.js"></script>
<script src="enjoyhint/help.js"></script>

<script>

document.addEventListener("DOMContentLoaded", function(event) { 
var acc = document.getElementsByClassName("accordion");
var panel = document.getElementsByClassName('panel');

for (var i = 0; i < acc.length; i++) {
    acc[i].onclick = function() {
        var setClasses = !this.classList.contains('active');
        setClass(acc, 'active', 'remove');
        setClass(panel, 'show', 'remove');

        if (setClasses) {
            this.classList.toggle("active");
            this.nextElementSibling.classList.toggle("show");
        }
    }
}

function setClass(els, className, fnName) {
    for (var i = 0; i < els.length; i++) {
        els[i].classList[fnName](className);
    }
}

});


// so it initializes the width.
closeNav();

</script>

</body>
</html>
'''
column_h = '''  <div class="imgcolumn">
'''
column_f = '''  </div>
'''

fig = '''
    <figure data-toggle="tooltip" id="___CAMPID___" onclick="copyTextToClipboard('___PODCASTRSS___', '___CAMPID___')" onmouseout="mouseOut('___CAMPID___')">
      <img class=scaled src="___IMAGE___" style="width:100%">
      <figcaption>___TITLE___</figcaption>
    </figure>
'''
max_cols = 8
col_len = len(camps) / max_cols + (1 if len(camps) % max_cols else 0)
list_page = list_page_header
camp_number = 1
basewidth = 420
for camp in camps:
    name = camp[0]
    expr = camp[1]
    ssns = None
    if len(camp) > 4:
        ssns = camp[4]
    else:
        expr2 = '' if len(camp) < 4 else (camp[3] + '.*')

        cmd = "sed -ne s/^.*href=\"\(" + expr + ".*mp3\)\".*" + expr2 + "$/\\1/p allsongs.html" 
        #print cmd
        ssns = subprocess.check_output(cmd.split())
    #print "sessions are: " + ssns
    #image_file = 'DAG.jpg'
    response = None
    image = LINK_URL + 'DAG.jpg'
    if len(camp) >= 3:
        image_file = camp[2]
        image = IMAGES_URL + image_file
        response = requests.get(image)
    else:
        cmd = "grep -i -m 1 " + name.replace(' ', '.*') + " images.html"
        try:
            image_line = subprocess.check_output(cmd.split())
            image_file = re.search(r'(?<=href=").*jpg(?=">)', image_line).group(0)
            image = IMAGES_URL + image_file
            #print image
            response = requests.get(image)
            if response.status_code != 200:
                image = LINK_URL + 'DAG.jpg'
        except subprocess.CalledProcessError, e:
            print str(e) 

    #cmd = "sed -ne s/^.*href=\"\(" + expr + ".*jpg\).*$/\\1/p allsongs.html" 
    folder = name.lower().replace(' ', '_').replace("'","").replace('?', '')

    if response and response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        image_path = os.path.join(folder, image_file).replace('%20', '_').replace('/_','/').replace('%3f','')
        if not os.path.exists(folder):
            os.makedirs(folder)
        img.save(image_path)
        image = LINK_URL + image_path   

    podcast = pod_header.replace('___TITLE___', name) \
                .replace('___LINK___', LINK_URL + folder) \
                .replace('___IMAGE___', image)
    tracknum = 1000
    for ssn in ssns.split():
        #print FILES_URL + ssn
        ssnTitle = ssn.split('.mp3')[0].split(expr, 1)[1].replace('%20', ' ')
        epis = episode.replace('___URL___', FILES_URL + ssn) \
            .replace('___EPISODE___', ssnTitle) \
            .replace('___TRACKORDER___', time.strftime('%M:%S', time.gmtime(tracknum)))
        #print epis
        podcast += epis
        tracknum -= 1

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
