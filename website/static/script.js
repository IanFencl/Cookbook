var ingredients = document.getElementById('ingredients');
var addMoreFields = document.getElementById('addMoreFields');
var removeFields = document.getElementById('removeFields');
var newFields = document.getElementById('newFields');
//export {getI}
addMoreFields.onclick = function() {
    document.getElementById("addMoreFields").addEventListener("click", myDiv());
    
}

var i = 1;
function myDiv() {
    var newDiv = '<br />'
    +'<div class="row">'
    +'<div class="col">'
    +'<input type="text" class="form-control" id="Ingredient' +i.toString() +'" name="Ingredient' +i.toString() +'" placeholder="Ingredient name" aria-label="Ingredient name">'
    +'</div>'
    +'<div class="col">'
    +' <input type="text" class="form-control" id="Amount' +i.toString() +'" name="Amount' +i.toString() +'" placeholder="Amount" aria-label="Amount">'
    +' </div>'
    +'<div class="col">'
    +'     <input type="text" class="form-control" id="Unit' +i.toString() +'" name="Unit' +i.toString() +'" placeholder="Unit" aria-label="Unit">'
    +'  </div>'
    +'  </div>'
    +'  </div>'

    document.getElementById("newFields").insertAdjacentHTML("beforeend", newDiv);

    i++;
    //add new i to getI
    var getI;
    document.getElementById("getI").value = i.toString();
    //alert(i.toString());
}

removeFields.onclick = function() {
    var input_tags = newFields.getElementsByClassName('row');
    if(input_tags.length > 1) {
        newFields.removeChild(input_tags[(input_tags.length) -1]);
        i--;
        //alert(i.toString());
        var getBR = newFields.getElementsByTagName('br');
        if (getBR.length >0) {
            newFields.removeChild(getBR[(getBR.length) -1]);
    }
    }
    else {
        alert("1 ingredient isn't a recipe >:(")
    }
}

/*function getI() {
    return i
}

function passI() {
    $.ajax({
        type: 'POST',
        url:'/add_recipe',
        dataType:'int',
        traditional: true,
        data: i,
        success: function() {
            getI()
        }

    })
}*/