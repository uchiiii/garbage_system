

document.getElementById('btn').onclick = function msgdsp(){
    if(confirm("ゴミ箱の量をリセットしますか?")){
        drawGraph();
    }else{
        alert("操作を取り消しました.")
    }
}


function drawGraph(){
    var pathname = location.pathname;
    if(pathname.lastIndexOf('/')>=0){
        var url = '/reset/' + pathname.substring(pathname.lastIndexOf('/')+1);
    }
    $.ajax({
        url : url,
        type : 'GET',
        dataType : 'json',
        success : function(res){
            pet_num = [];
            bin_num = [];
            can_num = [];
            label = [];
            //alert(res.pet_amount["2018/4"]); OK
            for(var item in res.pet_amount){
                label.push(item);
                pet_num.push(res.pet_amount[item]);
            }
            for(var item in res.bin_amount){
                bin_num.push(res.bin_amount[item]);
            }
            for(var item in res.can_amount){
                can_num.push(res.can_amount[item]);
            }
            data = {
                labels: label,
                datasets: [{
                    label: 'PET BOTTLE',
                    fill: false,
                    backgroundColor: "rgba(0,255,255,0.2)",
                    borderWidth: 2,
                    borderColor: "green",
                    pointBorderColor: "#fff",
                    pointBorderWidth: 2,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 2,
                    tension: 0,
                    data: pet_num
                }, {
                    label: 'BIN',
                    fill: false,
                    backgroundColor: "rgba(0,0,255,0.2)",
                    borderWidth: 2,
                    borderColor: "blue",
                    pointBorderColor: "#fff",
                    pointBorderWidth: 2,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 2,
                    tension: 0,
                    data: bin_num
                },{
                    label: 'CAN',
                    fill: false,
                    backgroundColor: "rgba(255,0,0,0.2)",
                    borderWidth: 2,
                    borderColor: "red",
                    pointBorderColor: "#fff",
                    pointBorderWidth: 2,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 2,
                    tension: 0,
                    data: can_num
                }]
            }
            
            $("canvas#myChart").remove();
            $("div.myChart").append('<canvas id="myChart" ></canvas>');
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: data
            });
        }
    })    
} 

