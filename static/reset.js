var barChartData = {
    labels : ["田中","山田","奥谷","ザビエル","おそ松","ピカチュウ","あひる"],
    datasets : [
        {
          fillColor : /*"#d685b0"*/"rgba(214,133,176,0.7)",
          strokeColor : /*"#d685b0"*/"rgba(214,133,176,0.7)",
          highlightFill: /*"#eebdcb"*/"rgba(238,189,203,0.7)",
          highlightStroke: /*"#eebdcb"*/"rgba(238,189,203,0.7)",
          data : [20,45,1,20,19,33,96]
        },
        {
          fillColor : /*"#7fc2ef"*/"rgba(127,194,239,0.7)",
          strokeColor : /*"#7fc2ef"*/"rgba(127,194,239,0.7)",
          highlightFill : /*"#a5d1f4"*/"rgba(165,209,244,0.7)",
          highlightStroke : /*"#a5d1f4"*/"rgba(165,209,244,0.7)",
          data : [2,54,77,32,9,78,95]
        }
      ]
  
    }
    window.onload = function(){
      var ctx = document.getElementById("chart").getContext("2d");
      window.myBar = new Chart(ctx).Bar(barChartData, {
        responsive : true,
        // アニメーションを停止させる場合は下記を追加
        /* animation : false */
      });
    }