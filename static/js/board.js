var chessboard = document.getElementById('chessboard');

var pieceType = new Map();
pieceType.set("r", "rook");
pieceType.set("n", "knight");
pieceType.set("b", "bishop");
pieceType.set("q", "queen");
pieceType.set("k", "king");
pieceType.set("p", "pawn");

var position = [];

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
  board = document.createElement('div');
  for (var row = 0; row < 8; row++) {
    var rowEl = document.createElement('tr');
    for (var cell = 0; cell < 8; cell++) { 
      
      var button = document.createElement('button');
      button.dataset.position = "" + row + cell;
      var cellEl = document.createElement('td');
      button.setAttribute('onclick', 'addPose(this)');
      button.value =
      button.onclick = function() {addPose(this);};
      cellEl.dataset.position = "" + row + cell;  
      button.appendChild(cellEl);
      rowEl.appendChild(button);
    }
    board.appendChild(rowEl);
    chessboard.appendChild(board);
  }
}

async function addPose(document) 
{
  position.push(document.dataset.position);
  if(position.length == 2) {
    console.log("position: " + position);

    var data = await fetch("/api/playPieces?from=" + position[0] + "&to=" + position[1])
    .then(response => {
      return response.json();
    })
    console.log(data);
    if(data == true) {
      console.log("success");
      resetBoard();
    }
    position = [];
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

async function placePieces () {
  piecePos = JSON.parse(await getBoardJson());
  for ([key, value] of Object.entries(piecePos)) {

    var pieceEl = document.querySelector('td[data-position="' + key + '"]');
    setPieceData(pieceEl, getPiecesColor(value), getPiecesType(value));
  }
}


async function start() {

  //createTablebuttons();
  createBoard();
  placePieces();

}

async function resetBoard()
{
  document.querySelector('div').remove();
  createBoard();
  placePieces();
}

start();