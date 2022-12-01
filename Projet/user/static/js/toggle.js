/******************toggle colonnes table ********* */
var coltitle = document.querySelector('.columntitle');
var col = document.querySelector('.column');
var a = document.querySelectorAll('.column a');
var i = document.querySelector('.column a i');


coltitle.addEventListener('click',function()
{col.classList.toggle('hide')
}
)

for( var i=0; i<a.length; i++)
{ a[i].addEventListener("click", () => {
this.classList.toggle('blue');
}
    )
}
