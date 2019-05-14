 var eh_instance = new EnjoyHint({});
 
 var help_steps = [
 {
	 "next #idthis": 'Each camp in <b>The Machaneh Directory</b> is a podcast on its own - a powerful, unique and immersive spiritual experience.'
 },
 {
	 "next #building_a_multiple_mega_church":"<text style='text-align: left'>Two easy steps:<br>" +
		"<li>First click or tap a camp thumbnail - its URL is copied.</li>" + 
		"<li>Then subscribe to it by URL in your podcast app</li>",
      'shape': 'circle',
      'radius': 100
 },
 {
    "next #idhelp": 'Not sure how to subscribe to a podcast by URL link?<br>Hints are available under help button.'
 },
 {
    "next #idsearch": 'Looking for a particular camp?<br>Scroll down for more thumbnails, or enter part of the name in search bar.'
 },
 {
    "click #idsearch": 'Consider adding this page to your home screen for easy access in the future.',
    "skipButton": {className: "sqip", text: "Got It!"}
 },
 ];
 
 eh_instance.set(help_steps);
 
 eh_instance.run();
