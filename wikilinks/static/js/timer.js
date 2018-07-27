  window.setTimeout("refresh()",500);
  function refresh()
  {
    console.log("lol");
    var xmlhttp;
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
      {
          CreateTimer("timer",parseInt(xmlhttp.responseText));
      }
    }
    xmlhttp.open("GET","/time",true);
    xmlhttp.send();
    return
  }
    
  //window.onload = CreateTimer("timer",{{t}});
  var Timer;
  var TotalSeconds;


  function CreateTimer(timer, Time) 
  {
    Timer = document.getElementById(timer);
    TotalSeconds = Time;

    UpdateTimer()
    window.setTimeout("Tick()", 1000);  
  }

  function Tick() 
  {
    if (TotalSeconds <= 0 || TotalSeconds>900)
    {
      window.location="/wiki/?x=timeup";
      return;
    }

    TotalSeconds -= 1;
    UpdateTimer()
    window.setTimeout("Tick()", 1000);
  }

  function UpdateTimer() 
  {
    Seconds=TotalSeconds;
    var Hours = Math.floor(Seconds / 3600);
    Seconds -= Hours * (3600);

    var Minutes = Math.floor(Seconds / 60);
    Seconds -= Minutes * (60);

    Hours=Hours%24

    var totalTime=Set(Hours)+":"+Set(Minutes)+":"+Set(Seconds); 

    Timer.innerHTML=totalTime;

    function Set(Time) {

    return (Time < 10) ? "0" + Time : + Time;

  }
}
