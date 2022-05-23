var chessboard = document.getElementById('chessboard');

var pieceType = new Map();
pieceType.set("r", "rook");
pieceType.set("n", "knight");
pieceType.set("b", "bishop");
pieceType.set("q", "queen");
pieceType.set("k", "king");
pieceType.set("p", "pawn");
gameIsOver = false;
var positionArr = [];
var currentPlayer = 1;
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

async function addPose(elem) 
{
  elem.color = "red";
  var position = elem.dataset.position;
  var pieceEl = elem.querySelector('td[data-position="' + position + '"]');
  var piece = pieceEl.className;
  console.log(piece);
  if(piece != '' || (piece == '' && positionArr.length > 0)) {
    console.log("yo")
    positionArr.push(elem.dataset.position);
    if(positionArr.length == 2) {
      console.log("position: " + positionArr);
      var url = new URL(window.location.href);
      var gameId = url.searchParams.get("gameId");
      console.log("gameId : " + gameId);
      var data = await fetch("/api/playPieces?from=" + positionArr[0] + "&to=" + positionArr[1]+ "&gameId=" + gameId)
      .then(response => {
        return response.json();
      })
      console.log(data);
      if(data == true) {
        console.log("success");
        await resetBoard();
        test = await isCheckMate()
        console.log("test"+test);

        if(test == true) {
          alert("Checkmate");
          const states = document.getElementById('states');
          states.innerHTML = "Le jeu est terminé, le joueur "+ currentPlayer + " à gagné";
        } else {
          currentPlayer = currentPlayer == 1 ? 2 : 1;
          const states = document.getElementById('states');
          states.innerHTML = "C'est au tour du joueur "+currentPlayer;
        }
        if(url.searchParams.get("type") == "Stockfish" || url.searchParams.get("type") == "minmax" || url.searchParams.get("type") == "minmaxBad") {
          console.log("url.searchParams.get(type) : " + url.searchParams.get("type"));
          var data = await fetch("/api/"+ url.searchParams.get("type") + "?gameId=" + gameId)
          .then(response => {
            return response.json();
          })
          console.log("response : " + data);
          await resetBoard();
          test = await isCheckMate()
          console.log("test"+test);
  
          if(test == true) {
            alert("Checkmate");
            const states = document.getElementById('states');
            states.innerHTML = "Le jeu est terminé, le joueur "+ currentPlayer + " à gagné";
          } else {
            currentPlayer = currentPlayer == 1 ? 2 : 1;
            const states = document.getElementById('states');
            states.innerHTML = "C'est au tour du joueur "+currentPlayer;
          }
        }
      }
      positionArr = [];
    }
  }
}

async function getBoardJson() {
  // get arguments from the url
  var url = new URL(window.location.href);
  var gameId = url.searchParams.get("gameId");
  console.log("gameId : " + gameId);
  var data = await fetch("/api/board?gameId=" + gameId)
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    return jsondata;});
  return data;
}

async function isCheckMate() {
  var url = new URL(window.location.href);
  var gameId = url.searchParams.get("gameId");
  var data = await fetch("/api/checkmate?gameId=" + gameId)
  .then(response => {
    return response.json();
  })
  .then(jsondata => {
    return jsondata;});
  console.log("checkmate : "+data);
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