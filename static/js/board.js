var chessboard = document.getElementById('chessboard');

var pieceType = new Map();
pieceType.set("r", "rook");
pieceType.set("n", "knight");
pieceType.set("b", "bishop");
pieceType.set("q", "queen");
pieceType.set("k", "king");
pieceType.set("p", "pawn");


function getPiecesType(piece) {
  return pieceType.get(piece.toLowerCase());
}

function getPiecesColor(piece) {
  if(piece == piece.toLowerCase()) {
    return 'white';
  }
  return 'black';
}


function createBoard() {
  for (var row = 0; row < 8; row++) {
    var rowEl = document.createElement('tr');
    for (var cell = 0; cell < 8; cell++) { 
      var cellEl = document.createElement('td');
      cellEl.dataset.position = "" + row + cell;  
      rowEl.appendChild(cellEl);
    }
    chessboard.appendChild(rowEl);
  }
}

async function getBoardJson() {
  var data = await fetch("/api/board")
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    return jsondata;});
  return data;
}

function setPieceData (el, color, type) {
  el.classname = ''; 
  el.classList.add(color); 
  el.classList.add(type); 
}

function resetBoard (piecePos) {

  for ([key, value] of Object.entries(piecePos)) {
    console.log("key: " + key + " value: " + value);
    var pieceEl = document.querySelector('td[data-position="' + key + '"]');
    setPieceData(pieceEl, getPiecesColor(value), getPiecesType(value));
  }
}

async function start() {
  piecePos = JSON.parse(await getBoardJson());

  createBoard();
  resetBoard(piecePos);
}

start();