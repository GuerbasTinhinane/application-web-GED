/***************RESPONSIVE*/ 

/*----------------nav bar ------------------*/
/*----LES VARIABLES----*/
const body = document.querySelector("body"),
  sidebar = body.querySelector(".sidebar"),
  toggle = body.querySelector(".toggle"),
  modeText = body.querySelector(".mode-text");


var ul = body.querySelector(".drop-down ul")
var li = body.querySelector(".nav-link.down ")
var np = document.querySelector(".nomprenom")
var icon = document.querySelector(".dropdown-btn")

var dropdownct =document.querySelector('.dropdownct-content')
var dropdownst =document.querySelector('.dropdownst-content')
var dropdownaj =document.querySelector('.dropdownaj-content')
var dropdownpds =document.querySelector('.dropdownpds-content')
var ast = document.querySelector('.ast')
var cst = document.querySelector('.cst')
var act = document.querySelector('.act')
var cct = document.querySelector('.cct')
var aaj = document.querySelector('.aaj')
var caj = document.querySelector('.caj')
var apds = document.querySelector('.apds')
var cpds = document.querySelector('.cpds')


var droppdown1=document.querySelector('.droppdown1')
var droppdown2=document.querySelector('.droppdown2')
var droppdown3=document.querySelector('.droppdown3')
var droppdown4=document.querySelector('.droppdown4')
var droppdown5=document.querySelector('.droppdown5')
var a1 = document.querySelector('.a1')
var a2 = document.querySelector('.a2')
var a3 = document.querySelector('.a3')
var a4 = document.querySelector('.a4')
var a5 = document.querySelector('.a5')
var a6 = document.querySelector('.a6')
var a7 = document.querySelector('.a7')
var a8 = document.querySelector('.a8')
var a9 = document.querySelector('.a9')
var a10 = document.querySelector('.a10')

var dropdownac = document.querySelector('.dropdownac-content')
var dropdownconv = document.querySelector('.dropdownconv-content')
var dropdownla= document.querySelector('.dropdownla-content')
var dropdownav = document.querySelector('.dropdownav-content')
var dropdownaop = document.querySelector('.dropdownaop-content')

var sousmenu =document.querySelectorAll('.sous-menu')
/*var label = document.querySelectorAll('.form form label')*/
var formst = document.querySelectorAll('#ajouterst')
var entete= document.querySelector('.entete')
var form = document.querySelectorAll('.form form')


var navlink = document.querySelectorAll('.droppdown')
var navlink2 = document.querySelectorAll('.navlink2')

var link2 = document.querySelector('.link2')
var link3 = document.querySelector('.link3')
var link4 = document.querySelector('.link4')
var link5 = document.querySelector('.link5')
var link6 = document.querySelector('.link6')
var link7 = document.querySelector('.link7')
var link8 = document.querySelector('.link8')
var slink1 = document.querySelector('.slink1')
var slink2 = document.querySelector('.slink2')
var slink3 = document.querySelector('.slink3')
var slink4 = document.querySelector('.slink4')
var slink5 = document.querySelector('.slink5')
/*----LES FONCTIONS-----*/

/*ouvrir et réduire nav bar + ajouter/consulter */
toggle.addEventListener("click", () => {
if (sidebar.classList.contains("close"))
{   sidebar.classList.remove("close")/*nav bare normale*/
toggle.style.right='20px'

act.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
cct.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
  dropdownct.style.position='relative';
  dropdownct.style.top='10px';
  dropdownct.style.left='30px';
  dropdownct.style.width='80%';
 
 /*ajouter /consulter grands titres*/ 
ast.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
cst.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
  dropdownst.style.position='relative';
  dropdownst.style.top='10px';
  dropdownst.style.left='30px';
  dropdownst.style.width='80%';

  
  aaj.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
  caj.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
  dropdownaj.style.position='relative';
  dropdownaj.style.top='10px';
  dropdownaj.style.left='30px';
  dropdownaj.style.width='80%';

  apds.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
  cpds.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
  dropdownpds.style.position='relative';
  dropdownpds.style.top='10px';
  dropdownpds.style.left='30px';
  dropdownpds.style.width='80%';
 
/*ajouter /consulter sous titres docs contractuels*/ 
a1.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
a2.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
dropdownconv.style.position='relative';
dropdownconv.style.top='15px';
dropdownconv.style.left='40px';
dropdownconv.style.width='60%';

a3.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
a4.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
dropdownav.style.position='relative';
dropdownav.style.top='15px';
dropdownav.style.left='40px';
dropdownav.style.width='60%';

a5.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
a6.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
dropdownla.style.position='relative';
dropdownla.style.top='15px';
dropdownla.style.left='40px';
dropdownla.style.width='60%';

a7.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
a8.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
dropdownac.style.position='relative';
dropdownac.style.top='15px';
dropdownac.style.left='40px';
dropdownac.style.width='73%';

a9.innerHTML="<i class='bx bx-list-plus'></i> Ajouter"
a10.innerHTML="<i class='bx bx-show-alt'></i> Consulter"
dropdownaop.style.position='relative';
dropdownaop.style.top='15px';
dropdownaop.style.left='40px';
dropdownaop.style.width='60%';

droppdown1.style.marginLeft='60px'
droppdown2.style.marginLeft='60px'
droppdown3.style.marginLeft='60px'
droppdown4.style.marginLeft='60px'
droppdown5.style.marginLeft='60px'

droppdown1.firstElementChild.innerHTML="Convention de <br> détachement"
droppdown2.firstElementChild.innerHTML="Avenant"
droppdown3.firstElementChild.innerHTML="Lettre accord"
droppdown4.firstElementChild.innerHTML="Accord"
droppdown5.firstElementChild.innerHTML="Accord d'operation"
/* masquer nom des icones nav bar normale*/


navlink[0].addEventListener('mouseover',function()
      { 
        link2.classList.remove('nohide')
        link2.classList.add('hide')

      })
     
 navlink[0].addEventListener('mouseleave',function(){
        {
          link2.classList.remove('nohide')
          link2.classList.add('hide')
        }
      }
      )

navlink[1].addEventListener('mouseover',function()
      { 
        link3.classList.remove('nohide')
          link3.classList.add('hide')

      })
     
navlink[1].addEventListener('mouseleave',function(){
        {
          link3.classList.remove('nohide')
          link3.classList.add('hide')
        }
      }
 )
 li.addEventListener('mouseover',function()
 { 
  link4.classList.remove('nohide')
  link4.classList.add('hide')
if (ul.classList.contains("show"))
{droppdown1.addEventListener('mouseenter',function()
{ 
  slink1.classList.remove('nohide')
  slink1.classList.add('hide')
  link4.classList.remove('nohide')
  link4.classList.add('hide')

})

droppdown1.addEventListener('mouseleave',function(){

    {
    slink1.classList.remove('nohide')
    slink1.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown2.addEventListener('mouseenter',function()
{ 
  slink2.classList.remove('nohide')
  slink2.classList.add('hide')
  link4.classList.remove('nohide')
  link4.classList.add('hide')

})

droppdown2.addEventListener('mouseleave',function(){
  {
    slink2.classList.remove('nohide')
    slink2.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown3.addEventListener('mouseenter',function()
{ 
  slink3.classList.remove('nohide')
  slink3.classList.add('hide')
  link4.classList.remove('nohide')
  link4.classList.add('hide')

})

droppdown3.addEventListener('mouseleave',function(){
  {
    slink3.classList.remove('nohide')
    slink3.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown4.addEventListener('mouseenter',function()
{ 
  slink4.classList.remove('nohide')
  slink4.classList.add('hide')
  link4.classList.remove('nohide')
  link4.classList.add('hide')

})

droppdown4.addEventListener('mouseleave',function(){
  {
    slink4.classList.remove('nohide')
    slink4.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown5.addEventListener('mouseenter',function()
{ 
  slink5.classList.remove('nohide')
  slink5.classList.add('hide')
  link4.classList.remove('nohide')
  link4.classList.add('hide')

})

droppdown5.addEventListener('mouseleave',function(){
  {
    slink5.classList.remove('nohide')
    slink5.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)
}

 })

li.addEventListener('mouseleave',function(){
   {
     link4.classList.remove('nohide')
     link4.classList.add('hide')
   }
 }
)



navlink[2].addEventListener('mouseover',function()
      { 

link5.classList.remove('nohide')
link5.classList.add('hide')

      })
     
navlink[2].addEventListener('mouseleave',function(){
        {
          link5.classList.remove('nohide')
          link5.classList.add('hide')
        }
      }
      )
navlink[3].addEventListener('mouseover',function()
{
          link6.classList.remove('nohide')
          link6.classList.add('hide')

      })
     
 navlink[3].addEventListener('mouseleave',function(){
        {
          link6.classList.remove('nohide')
          link6.classList.add('hide')
        }
      }
      )
navlink2[0].addEventListener('mouseover',function()
      {
                link7.classList.remove('nohide')
                link7.classList.add('hide')
      
            })
           
navlink2[0].addEventListener('mouseleave',function(){
              {
                link7.classList.remove('nohide')
                link7.classList.add('hide')
              }
            }
            )
navlink2[1].addEventListener('mouseover',function()
            {
                      link8.classList.remove('nohide')
                      link8.classList.add('hide')
            
                  })
                 
                  navlink2[1].addEventListener('mouseleave',function(){
                    {
                      link8.classList.remove('nohide')
                      link8.classList.add('hide')
                    }
                  }
                  )
                  
/*nom prenom du nav bar*/
np.style.left='-250px'
/*element formulaire*/
/*
for( var i=0; i<form.length; i++)
{form[i].style.width='1000px'}
entete.style.width='1050px'*/
/*
for( var i=0; i<label.length; i++)
{label[i].style.marginLeft='5%'}*/



}
else/*nav bar réduite*/
{    sidebar.classList.add("close")
toggle.style.right='-30px'




ast.innerHTML="<i class='bx bx-list-plus'></i>"
cst.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownst.style.left='15px';
dropdownst.style.width='30px';

act.innerHTML="<i class='bx bx-list-plus'></i>"
cct.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownct.style.left='15px';
dropdownct.style.width='30px';

aaj.innerHTML="<i class='bx bx-list-plus'></i>"
caj.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownaj.style.left='15px';
dropdownaj.style.width='30px';

apds.innerHTML="<i class='bx bx-list-plus'></i>"
cpds.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownpds.style.left='15px';
dropdownpds.style.width='30px';


droppdown1.style.margin='0px'
droppdown2.style.margin='0px'
droppdown3.style.margin='0px'
droppdown4.style.margin='0px'
droppdown5.style.margin='0px'

droppdown1.firstElementChild.innerHTML="<i class='bx bx-file-blank iconx dropbtn1'></i>"
droppdown2.firstElementChild.innerHTML="<i class='bx bx-file-blank iconx dropbtn2'></i>"
droppdown3.firstElementChild.innerHTML="<i class='bx bx-file-blank iconx dropbtn3'></i>"
droppdown4.firstElementChild.innerHTML="<i class='bx bx-file-blank iconx dropbtn4'></i>"
droppdown5.firstElementChild.innerHTML="<i class='bx bx-file-blank iconx dropbtn5'></i>"


a1.innerHTML="<i class='bx bx-list-plus'></i>"
a2.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownconv.style.left='20px';
dropdownconv.style.width='20px';

a3.innerHTML="<i class='bx bx-list-plus'></i>"
a4.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownav.style.left='20px';
dropdownav.style.width='20px';

a5.innerHTML="<i class='bx bx-list-plus'></i>"
a6.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownla.style.left='20px';
dropdownla.style.width='20px';

a7.innerHTML="<i class='bx bx-list-plus'></i>"
a8.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownac.style.left='20px';
dropdownac.style.width='20px';

a9.innerHTML="<i class='bx bx-list-plus'></i>"
a10.innerHTML="<i class='bx bx-show-alt'></i>"
dropdownaop.style.left='20px';
dropdownaop.style.width='20px';


/*nom des icones nav bar réduite*/


navlink[0].addEventListener('mouseover',function()
      { 
link2.classList.remove('hide')
link2.classList.add('nohide')

      })
     
 navlink[0].addEventListener('mouseleave',function(){
        {
          link2.classList.remove('nohide')
          link2.classList.add('hide')
        }
      }
      )

navlink[1].addEventListener('mouseover',function()
      { 
link3.classList.remove('hide')
link3.classList.add('nohide')

      })
     
navlink[1].addEventListener('mouseleave',function(){
        {
          link3.classList.remove('nohide')
          link3.classList.add('hide')
        }
      }
 )
 li.addEventListener('mouseover',function()
 { 
link4.classList.remove('hide')
link4.classList.add('nohide')
if (ul.classList.contains("show"))
{
droppdown1.addEventListener('mouseenter',function()
{ 
  slink1.classList.remove('hide')
  slink1.classList.add('nohide')
  link4.classList.remove('hide')
  link4.classList.add('nohide')

})

droppdown1.addEventListener('mouseleave',function(){
  {
    slink1.classList.remove('nohide')
    slink1.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown2.addEventListener('mouseenter',function()
{ 
  slink2.classList.remove('hide')
  slink2.classList.add('nohide')
  link4.classList.remove('hide')
  link4.classList.add('nohide')

})

droppdown2.addEventListener('mouseleave',function(){
    slink2.classList.remove('nohide')
    slink2.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
}
)

droppdown3.addEventListener('mouseenter',function()
{ 
  slink3.classList.remove('hide')
  slink3.classList.add('nohide')
  link4.classList.remove('hide')
  link4.classList.add('nohide')

})

droppdown3.addEventListener('mouseleave',function(){
    slink3.classList.remove('nohide')
    slink3.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
}
)

droppdown4.addEventListener('mouseenter',function()
{ 
  slink4.classList.remove('hide')
  slink4.classList.add('nohide')
  link4.classList.remove('hide')
   link4.classList.add('nohide')

})

droppdown4.addEventListener('mouseleave',function(){
  {
    slink4.classList.remove('nohide')
    slink4.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)

droppdown5.addEventListener('mouseenter',function()
{ 
  slink5.classList.remove('hide')
  slink5.classList.add('nohide')
  link4.classList.remove('hide')
  link4.classList.add('nohide')

})

droppdown5.addEventListener('mouseleave',function(){
  {
    slink5.classList.remove('nohide')
    slink5.classList.add('hide')
    link4.classList.remove('nohide')
    link4.classList.add('hide')
  }
}
)
}

 })

li.addEventListener('mouseleave',function(){
   {
     link4.classList.remove('nohide')
     link4.classList.add('hide')
   }
 }
)



navlink[2].addEventListener('mouseover',function()
      { 
        if (ul.classList.contains("show"))
        {link5.style.top='455px'
        }
        else
{link5.style.top='260px'
}
link5.classList.remove('hide')
link5.classList.add('nohide')

      })
     
navlink[2].addEventListener('mouseleave',function(){
        {
          link5.classList.remove('nohide')
          link5.classList.add('hide')
        }
      }
      )
navlink[3].addEventListener('mouseover',function()
      {  if (ul.classList.contains("show"))
      {
      link6.style.top='510px'}
      else
{
link6.style.top='310px'}
link6.classList.remove('hide')
link6.classList.add('nohide')

      })
     
 navlink[3].addEventListener('mouseleave',function(){
        {
          link6.classList.remove('nohide')
          link6.classList.add('hide')
        }
      }
      )
navlink2[0].addEventListener('mouseover',function()
      { 
if (ul.classList.contains("show"))
        {link7.style.top='562px'
        }
        else
{link7.style.top='370px'
}
link7.classList.remove('hide')
link7.classList.add('nohide')

      })
     
navlink2[0].addEventListener('mouseleave',function(){
        {
          link7.classList.remove('nohide')
          link7.classList.add('hide')
        }
      }
      )
navlink2[1].addEventListener('mouseover',function()
      { 
        if (ul.classList.contains("show"))
        {link8.style.top='615px'
        }
        else
{link8.style.top='425px'
}
link8.classList.remove('hide')
link8.classList.add('nohide')

      })
     
navlink2[1].addEventListener('mouseleave',function(){
        {
          link8.classList.remove('nohide')
          link8.classList.add('hide')
        }
      }
      )
      
np.style.left='-80px'
/*element formulaire*/
/*for( var i=0; i<form.length; i++)
{form[i].style.width='1150px'}
entete.style.width='1200px'*/
/*
for( var i=0; i<label.length; i++)
{label[i].style.marginLeft='100px'}*/
}


});



/*sous-menu docs contractuels*/
li.addEventListener("click", function(){

  if (ul.classList.contains("show"))/*sous-menu fermé*/
      {
        ul.classList.remove("show")
        ul.classList.add('hide')
        li.style.background='none'
        icon.classList.remove('bxs-chevron-up')
        icon.classList.add('bxs-chevron-down')
        ul.style.height='0px'
      }
  else 
      { /*sous-menu ouvert*/
        ul.classList.remove("hide")
        ul.classList.add('show')
        li.style.background='#f4f0ec'
        icon.classList.remove('bxs-chevron-down')
        icon.classList.add('bxs-chevron-up')
        ul.style.height='195px'

      }})

/*hauteur du sous menu docs contracuels*/

droppdown1.addEventListener('mouseenter',function()
      { 
ul.style.height='245px'

      })
     
      droppdown1.addEventListener('mouseleave',function(){
        {
        ul.style.height='180px'
        }
      }
      )

      droppdown2.addEventListener('mouseenter',function(){
        {ul.style.height='245px'
}
      })
      droppdown2.addEventListener('mouseleave',function(){
        {
        ul.style.height='180px'}   
      })
      
      droppdown3.addEventListener('mouseenter',function(){
        {ul.style.height='245px'}
      })

      droppdown3.addEventListener('mouseleave',function(){
        {ul.style.height='180px'}    
      })
      
      droppdown4.addEventListener('mouseenter',function(){
        {ul.style.height='245px'}
      })

      droppdown4.addEventListener('mouseleave',function(){
        {
        ul.style.height='180px'}   
      })

      droppdown5.addEventListener('mouseenter',function(){
        {ul.style.height='245px'}
      })

      droppdown5.addEventListener('mouseleave',function(){
        {
        ul.style.height='180px'}   
      })



  /*-----------MENU-------------*/
  var sousheader=document.querySelector('.sous-header') 
  var downarrow = document.querySelector('header .bxs-down-arrow') 
  
  downarrow.addEventListener('click',function(){
    if (sousheader.classList.contains('afficher'))
    {sousheader.classList.remove('afficher')
    downarrow.style.color='#707070'
    sousheader.classList.add('masquer')
    
    }
    else
    {sousheader.classList.remove('masquer')
    downarrow.style.color='#ff8c00'
      sousheader.classList.add('afficher')
    }
  })
    

  var iconplus1 = document.querySelector('.plus1')
  var formop = document.querySelector('.formop')
 
 iconplus1.addEventListener('click', function(){
 formop.classList.toggle('hide')
 }
 )

/***********************************************************/


var plus2 = document.querySelector('.plus2')
var formpart = document.querySelector('.formpart')

plus2.addEventListener('click', function(){
formpart.classList.toggle('hide')
}
)
/*---------------------tableau--------------------- */










/******************************************************** */
