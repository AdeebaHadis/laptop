(document).ready(funcyion(){
    $('.text').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"bounceIN",
        }
        out:{
            effect:"bounceout",
        },
        });

 var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 640,
    height: 200,
    style:"ios9",
    amplitude:"1",
    speed:"0.30",
    AutoStart:"true"
  });


$('.siri-message').textillate({
        loop:true,
        sync:true,
        in:{
            effect:"fadeInUp",
        }
        out:{
            effect:"fadeOutUp",
        },
        });


    });
});$
