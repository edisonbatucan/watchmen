const sidenav = document.getElementById("sidenav-1");
const sidenavInstance = mdb.Sidenav.getInstance(sidenav);

let innerWidth = null;

const setMode = (e) => {
  // Check necessary for Android devices
  if (window.innerWidth === innerWidth) {
    return;
  }

  innerWidth = window.innerWidth;

  if (window.innerWidth < 1400) {
    sidenavInstance.changeMode("over");
    sidenavInstance.hide();
  } else {
    sidenavInstance.changeMode("side");
    sidenavInstance.show();
  }
};

setMode();

const slimInstance = new mdb.Sidenav(document.getElementById('sidenav-1'));
slimInstance.show();

document.getElementById('sidenav-1').addEventListener('mouseover', () => {
  slimInstance.toggleSlim();
  document.getElementById('main-navbar').style.paddingLeft = "240px";
})
document.getElementById('sidenav-1').addEventListener('mouseout', () => {
  slimInstance.toggleSlim();
  if(window.matchMedia("(min-width: 1400px)"))
    document.getElementById('main-navbar').style.paddingLeft = "70px";
  else {
    document.getElementById('main-navbar').style.paddingLeft = "0px";
    alert("as")
  }
})
// Event listeners
window.addEventListener("resize", setMode);

const data = {
  columns: ['Name', 'Position', 'Office', 'Age', 'Start date', 'Salary'],
  rows: [
    ['Tiger Nixon', 'System Architect', '	Edinburgh', 61, '2011/04/25', '$320,800'],
    ['Sonya Frost', 'Software Engineer', 'Edinburgh', 23, '2008/12/13', '$103,600'],
    ['Jena Gaines', 'Office Manager', 'London', 30, '2008/12/19', '$90,560'],
    ['Quinn Flynn', 'Support Lead', 'Edinburgh', 22, '2013/03/03', '$342,000'],
    ['Charde Marshall', 'Regional Director', 'San Francisco', 36, '2008/10/16', '$470,600'],
    ['Haley Kennedy', 'Senior Marketing Designer', 'London', 43, '2012/12/18', '$313,500'],
    ['Tatyana Fitzpatrick', 'Regional Director', 'London', 19, '2010/03/17', '$385,750'],
    ['Michael Silva', 'Marketing Designer', 'London', 66, '2012/11/27', '$198,500'],
    ['Paul Byrd', 'Chief Financial Officer (CFO)', 'New York', 64, '2010/06/09', '$725,000'],
    ['Gloria Little', 'Systems Administrator', 'New York', 59, '2009/04/10', '$237,500'],
  ],
};

const searchInstance = new mdb.Datatable(document.getElementById('datatable'), data)

document.getElementById('datatable-search-input').addEventListener('input', (e) => {
  searchInstance.search(e.target.value);
});

function exportTableToExcel(tableID, filename = ''){
  var downloadLink;
  var dataType = 'application/vnd.ms-excel';
  var tableSelect = document.getElementById(tableID);
  var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
  
  // Specify file name
  filename = filename?filename+'.xls':'excel_data.xls';
  
  // Create download link element
  downloadLink = document.createElement("a");
  
  document.body.appendChild(downloadLink);
  
  if(navigator.msSaveOrOpenBlob){
      var blob = new Blob(['\ufeff', tableHTML], {
          type: dataType
      });
      navigator.msSaveOrOpenBlob( blob, filename);
  }else{
      // Create a link to the file
      downloadLink.href = 'data:' + dataType + ', ' + tableHTML;
  
      // Setting the file name
      downloadLink.download = filename;
      
      //triggering the function
      downloadLink.click();
  }
}
