function fallbackCopyTextToClipboard(text, element_id) {
  var textArea = document.createElement("textarea");
  textArea.value = text;
  document.body.appendChild(textArea);
  
  if (navigator.userAgent.match(/ipad|ipod|iphone/i)) {
    textArea.contentEditable = true;
    textArea.readOnly = false;
    // create a selectable range
    var range = document.createRange();
    range.selectNodeContents(textArea);

    // select the range
    var selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    textArea.setSelectionRange(0, 999999);
  } else {
    //textArea.readOnly = true;
    console.log("in non IOS zone");
    //textArea.focus();
    textArea.select();
  }
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
  //if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text, element_id);
    return;
  //}
  navigator.clipboard.writeText(text).then(function() {
    console.log('Async: Copying to clipboard was successful!');
  }, function(err) {
    console.error('Async: Could not copy text: ', err);
  });
}

function mouseOut(element_id) {
    $('[data-toggle="tooltip"]').tooltip('destroy')
}

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip({title: 'Copied RSS feed. Go paste it into your podcast app', trigger: 'click'})
    setTimeout(function(){
        $('[data-toggle="tooltip"]').tooltip('destroy')
    }, 3000);
});
