VF = Vex.Flow;

// svg 렌더러를 만들고 이름이 boo인 DIV 요소에 붙임
//var div = document.getElementById("boo");
//var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);

// canvas 렌더러를 만듬
var canvas = document.getElementById("myCanvas");
var renderer = new Vex.Flow.Renderer(canvas, Vex.Flow.Renderer.Backends.CANVAS); 

// 렌더링 방법 설정
renderer.resize(500, 500);
var context = renderer.getContext();
context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

// 너비가 400인 오선지를 캔버스의 10,40 위치에 만든다
var stave = new VF.Stave(10, 40, 800);

// 음자리표와 박자 기호를 추가
stave.addClef("treble").addTimeSignature("4/4");

// 렌더링 방법에 연결뒤 그리기 
stave.setContext(context).draw();

// 음표들을 만든다
var notes = [
  // A quarter-note C.
  new VF.StaveNote({ keys: ["c/4"], duration: "q" }),

  // A quarter-note D.
  new VF.StaveNote({ keys: ["d/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["e/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["f/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["g/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["a/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["b/4"], duration: "q" }),
  new VF.StaveNote({ keys: ["c/5"], duration: "q" }),

  // A quarter-note rest. Note that the key (b/4) specifies the vertical
  // position of the rest.
  // new VF.StaveNote({ keys: ["b/4"], duration: "qr" }),

  // // A C-Major chord.
  // new VF.StaveNote({ keys: ["c/4", "e/4", "g/4"], duration: "q" }),
  // new VF.StaveNote({ keys: ["c/4"], duration: "q" }),

  // // A quarter-note D.
  // new VF.StaveNote({ keys: ["d/4"], duration: "q" }),

  // // A quarter-note rest. Note that the key (b/4) specifies the vertical
  // // position of the rest.
  // new VF.StaveNote({ keys: ["b/4"], duration: "qr" }),

  // // A C-Major chord.
  // new VF.StaveNote({ keys: ["c/4", "e/4", "g/4"], duration: "q" })
];

// 4/4 성부를 만들고 위의 음표들을 추가한다
var voice = new VF.Voice({num_beats: 8,  beat_value: 4});
voice.addTickables(notes);

// 음표들을 400픽셀로 조정한다
var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);

// 성부 렌더링
voice.draw(context, stave);