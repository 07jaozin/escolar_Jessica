const menuToggle = document.querySelectorAll('#menu_toggle');
const header = document.querySelector('header');
const a = document.querySelectorAll('.nav_link');
const aula = document.querySelectorAll('.aulas');
const seta =document.querySelectorAll('.bx-seta');

seta.forEach((seta, index) => {
    seta.addEventListener("click", () => {
        
        aula[index].classList.toggle("visivel");
        const valorClass = seta.className;
        console.log(valorClass)
        if(valorClass === 'bx bx-seta bx-chevron-right'){
            seta.classList.remove('bx-chevron-right');
            seta.classList.add('bx-chevron-down');
        }
        else{
            seta.classList.remove('bx-chevron-down');
            seta.classList.add('bx-chevron-right');
           
        }
    });
});


a.forEach( links =>  {
   links.addEventListener("click", () => header.classList.remove("showMenu"));
}
)

menuToggle.forEach( toggler => {
    toggler.addEventListener("click", () => header.classList.toggle("showMenu"));
})
document.querySelector('#fisica').addEventListener("click", () => {
    window.location.href = '/fisica'
})
document.querySelector('#financeira').addEventListener("click", () => {
    window.location.href = '/educacao_financeira'
})
document.querySelector('#Matematica').addEventListener("click", () => {
    window.location.href = '/matematica'
})