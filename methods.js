function jqid( myid ) {
  return "#" + myid.replace( /(:|\.|\[|\]|,|=|@|\/)/g, "\\$1" );	 
}

function fallbackCopyTextToClipboard(text, element_id) {
  var textArea = document.createElement("textarea");
  textArea.value = text;
  document.body.appendChild(textArea);
  
  if (navigator.userAgent.match(/ipad|ipod|iphone/i)) {
    textArea.style.opacity = '0';
    textArea.style.zIndex = "-1";
    textArea.style.right = "0px";
    textArea.style.height = "1px";
    textArea.style.width = "1px";
    textArea.style.pointerEvents = "none";
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

var timeout;
function copyTextToClipboard(text, element_id) {
    clearTimeout(timeout);
  //if (!navigator.clipboard) {
    fallbackCopyTextToClipboard(text, element_id);
    console.log($(jqid(element_id)).length + ' elements found');
    $(jqid(element_id)).tooltip({title: 'Podcast link copied. Go subscribe by URL in your podcast app', trigger: 'manual', placement: 'top'})
    $(jqid(element_id)).tooltip('show');
    timeout = setTimeout(function(){$(jqid(element_id)).tooltip('hide')}, 3000);
    return;
//  }
//  navigator.clipboard.writeText(text).then(function() {
//    console.log('Async: Copying to clipboard was successful!');
//  }, function(err) {
//    console.error('Async: Could not copy text: ', err);
//  });
}

function mouseOut(element_id) {
    clearTimeout(timeout);
    $(jqid(element_id)).tooltip('hide')
}



function campSearch() {
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById("idsearch");
    filter = input.value.toUpperCase();
    ul = document.getElementById("allcamps");
    li = ul.getElementsByTagName("figure");
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("figcaption")[0];
        txtValue = a.textContent || a.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function openNav() {
  el = document.getElementById("mySidenav");
  if (el.style.width == "0px") {
    el.style.width = "350px";
  } else {
    el.style.width = "0px";
  }
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0px";
}
