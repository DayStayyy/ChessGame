var chessboard = document.getElementById('chessboard');
var space = 1;
for (var row = 0; row < 8; row++) {
  var rowEl = document.createElement('tr');
  for (var cell = 0; cell < 8; cell++) { 
    var cellEl = document.createElement('td');
    cellEl.dataset.position = toString(row)+toString(cell); // Each square on the board needs a way to be identified. ex. <td data-position="1"></td>
    rowEl.appendChild(cellEl);
    space++; 
  }
  chessboard.appendChild(rowEl);
}


var initialPieces = [
  { position: 1, color: 'black', type: 'rook' },
  { position: 2, color: 'black', type: 'knight' },
  { position: 3, color: 'black', type: 'bishop' },
  { position: 4, color: 'black', type: 'queen' },
  { position: 5, color: 'black', type: 'king' },
  { position: 6, color: 'black', type: 'bishop' },
  { position: 7, color: 'black', type: 'knight' },
  { position: 8, color: 'black', type: 'rook' },
  { position: 9, color: 'black', type: 'pawn' },
  { position: 10, color: 'black', type: 'pawn' },
  { position: 11, color: 'black', type: 'pawn' },
  { position: 12, color: 'black', type: 'pawn' },
  { position: 13, color: 'black', type: 'pawn' },
  { position: 14, color: 'black', type: 'pawn' },
  { position: 15, color: 'black', type: 'pawn' },
  { position: 16, color: 'black', type: 'pawn' },
  { position: 49, color: 'white', type: 'pawn' },
  { position: 50, color: 'white', type: 'pawn' },
  { position: 51, color: 'white', type: 'pawn' },
  { position: 52, color: 'white', type: 'pawn' },
  { position: 53, color: 'white', type: 'pawn' },
  { position: 54, color: 'white', type: 'pawn' },
  { position: 55, color: 'white', type: 'pawn' },
  { position: 56, color: 'white', type: 'pawn' },
  { position: 57, color: 'white', type: 'rook' },
  { position: 58, color: 'white', type: 'knight' },
  { position: 59, color: 'white', type: 'bishop' },
  { position: 60, color: 'white', type: 'queen' },
  { position: 61, color: 'white', type: 'king' },
  { position: 62, color: 'white', type: 'bishop' },
  { position: 63, color: 'white', type: 'knight' },
  { position: 64, color: 'white', type: 'rook' },
];

function setPieceData (el, color, type) {
  el.classname = ''; // This clears out any classes on the current <td>
  el.classList.add(color); // Add the class of either black or white
  el.classList.add(type); // Add the class of the piece: king, queen, rook, bishop, knight, or pawn
}

function resetBoard () {
  initialPieces.forEach(function(piece) {
    // This code will loop through every piece that was in the array initialPieces, use the position number for each piece
    // to find which cell on the <table> chessboard should hold the piece, and then send the correct piece information to
    // the function setPieceData
    var pieceEl = document.querySelector('td[data-position="' + piece.position + '"]');
    // This is the fanciest selector I'm using. It grabs a specific cell by combining strings together. For example: If I
    // wanted to get the cell with a position of 9, it ultimately looks like this document.querySelector('td[data-position="9"]')
    // which would make available to javascript the following html element <td data-position="9"></td>
    setPieceData(pieceEl, piece.color, piece.type);
  });
};

resetBoard();