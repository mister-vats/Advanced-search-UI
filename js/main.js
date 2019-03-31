var input = document.getElementById('comboSearch');
var cwmain = document.getElementById('cwMain');
var extendedsearch = document.getElementById('extendedSearch');
  input.addEventListener('keyup',function(e){
    if(e.which == 13){
        var inputVal = input.value;
        input.style.display = "none";
        input.parentElement.className += " morphing";
        setTimeout(function(){ extendedsearch.className += " show" }, 500);
        setTimeout(function(){ cwmain.className += " sliding" }, 800);

        
    }
});
