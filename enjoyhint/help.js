 var eh_instance = new EnjoyHint({});
 
 var help_steps = [
 {
	 "next #idthis": 'Each camp in <b>The Machaneh Directory</b> is a podcast on its own - a new creative way to use the podcast concept.<br>Allow me to guide you through the features.',
    "nextButton": {className: "nex", text: "Sure!"},
    "skipButton": {className: "sqip", text: "Nope"},
    'textColor': '255,255,100'
 },
 {
	 "next #building_a_multiple_mega_church":"<text style='text-align: left'>Two easy steps:<br>" +
		"<li>One click or quick tap on a camp thumbnail copies its URL - a confirmation message pops us for 3 seconds.</li>" + 
		"<li>Then subscribe to it by URL in your podcast app - NOT THE SAME AS searching for a podcast</li>",
      'shape': 'circle',
      'radius': 80,
      'textColor': '255,255,100',
      'z-index': 2
 },
 {
      "next #idhelp": 'Step by step instruction for subscribing by URL for various podcast apps are available under this button.',
      'shape': 'circle',
      'radius': 40,
      'textColor': '255,255,100',
      'z-index': 2
 },
 {
      "next #idsearch": 'Looking for a particular camp?<br>Scroll down for more thumbnails, or enter part of the name in search bar.',
      'textColor': '255,255,100',
      'shape': 'circle',
      'radius': 40,
      'z-index': 2
 },
 {
      "click #idthis": 'That\'s it. Now you can subsribe to a camp podcast, delete it when done, add it back later, etc.<br>Consider adding this page to your home screen for easy access in the future.',
      "skipButton": {className: "sqip", text: "Got It!"}
 },
 ];
 
 eh_instance.set(help_steps);
 
 eh_instance.run();
