 var eh_instance = new EnjoyHint({});
 
 var help_steps = [
 {
	 "next #idthis": 'Each camp in the directory is a podcast on its own - a world where you can enjoy an immersive spiritual experience.'
 },
 {
	 "next #loyalty_and_the_mega_church":"<text style='text-align: left'>Two easy steps:<br>" +
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
    "click #idsearch": 'Consider adding this page on your `home screen` if your browser is capable.',
    "skipButton": {className: "sqip", text: "Got It!"}
 },
 ];
 
 eh_instance.set(help_steps);
 
 eh_instance.run();
