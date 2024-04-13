// screens
let mainScreen = document.getElementById('main_screen')
let storageScreen = document.getElementById('storage_screen')

// Кнопки
let btnStorage = document.getElementById('storage_btn')



function getStorage () {
    mainScreen.classList.remove('visible_main_screen')
    mainScreen.classList.add('hide')
    storageScreen.classList.remove('hide')
    storageScreen.classList.add('visible_storage_screen')
}