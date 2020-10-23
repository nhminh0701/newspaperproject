const moreHeaderBtn = document.querySelector('.more-btn');
const collapseToggler = document.querySelector('.collapse-toggler');
const collapsableMenu = document.querySelector('.collapsable');

function toggleCollapsableMenu(event) {
    if (event.target.classList.contains('selecting')) {
        event.target.classList.remove('selecting');
        collapsableMenu.classList.add('collapsed');
    } else {
        event.target.classList.add('selecting');
        collapsableMenu.classList.remove('collapsed');
    }
}

moreHeaderBtn.addEventListener('click', function () {
    if (moreHeaderBtn.classList.contains('selecting')) {
        moreHeaderBtn.classList.remove('selecting');
        collapseToggler.classList.remove('selecting');
        collapsableMenu.classList.add('collapsed');
    } else {
        moreHeaderBtn.classList.add('selecting');
        collapseToggler.classList.add('selecting');
        collapsableMenu.classList.remove('collapsed');
    }
});

collapseToggler.addEventListener('click', function () {
    if (collapseToggler.classList.contains('selecting')) {
        moreHeaderBtn.classList.remove('selecting');
        collapseToggler.classList.remove('selecting');
        collapsableMenu.classList.add('collapsed');
    } else {
        moreHeaderBtn.classList.add('selecting');
        collapseToggler.classList.add('selecting');
        collapsableMenu.classList.remove('collapsed');
    }
});
