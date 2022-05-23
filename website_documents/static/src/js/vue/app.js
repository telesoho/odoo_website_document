// Registering the Button plugin.
Vue.use(ejs.filemanager.FileManagerPlugin, ejs.filemanager.NavigationPane, ejs.filemanager.Toolbar, ejs.filemanager.DetailsView, ejs.filemanager.FileManagerComponent);

/**
 * File Manager full functionalities sample
 */
// let hostUrl = 'http://localhost:8090/';
// // let hostUrl = '/fapi/';

// var app = new Vue({
//     el: '#app',
//     provide: {
//         filemanager: [ejs.filemanager.NavigationPane, ejs.filemanager.DetailsView, ejs.filemanager.Toolbar]
//     },
//     data: {
//         ajaxSettings:
//         {
//             url: hostUrl,
//             getImageUrl: hostUrl + 'GetImage',
//             uploadUrl: hostUrl + 'Upload',
//             downloadUrl: hostUrl + 'Download'
//         },
//         view: "Details"
//     }
// })

/**
 * File Manager full functionalities sample
 */
let hostUrl = 'https://ej2-aspcore-service.azurewebsites.net/';

var app = new Vue({
    el: '#app',
    provide: {
        filemanager: [ejs.filemanager.NavigationPane, ejs.filemanager.DetailsView, ejs.filemanager.Toolbar]
    },
    data: {
        ajaxSettings:
        {
            url: hostUrl + 'api/FileManager/FileOperations',
            getImageUrl: hostUrl + 'api/FileManager/GetImage',
            uploadUrl: hostUrl + 'api/FileManager/Upload',
            downloadUrl: hostUrl + 'api/FileManager/Download'
        },
        view: "Details"
    }
})
