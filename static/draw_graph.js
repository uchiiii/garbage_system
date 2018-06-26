jQuery(function ($) {
    $.PeriodicalUpdater('/draw_table',{
    //  オプション設定
        method: 'get',      // 送信リクエストURL
        minTimeout: 10000,  // 送信インターバル(ミリ秒)
        type: 'json',       // xml、json、scriptもしくはhtml (jquery.getやjquery.postのdataType)
        multiplier:1,       // リクエスト間隔の変更
        maxCalls: 0         //　リクエスト回数（0：制限なし）
    },
    function (res){
        $('table#table tr:nth-child(2) td:nth-child(1)').text(res.num_pet);
        $('table#table tr:nth-child(2) td:nth-child(2)').text(res.num_bin);
        $('table#table tr:nth-child(2) td:nth-child(3)').text(res.num_can);

    });
});

window.onload = function drawGraph(){
    $.ajax({
        url : '/draw_graph',
        type : 'GET',
        dataType : 'json',
        success : function(res){
            //alert(res.pet_amount["2018/4"]); OK
            pet_num = [];
            bin_num = [];
            can_num = [];
            label = [];
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
            dataset = {
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
            
            var ctx = document.getElementById("myChart").getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: dataset
            });
        }
    })

    
    
} 

