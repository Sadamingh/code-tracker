"use strict";

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var easy_perc = data.easySolved / data.totalEasy * 100
        var easy_count = data.easySolved
        $('#easycount').append(`<h5>Easy</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-success\" role=\"progressbar\" aria-valuenow=\"` + String(easy_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(easy_perc) + `%\"></div>` + String(easy_count) + "</div>")
    }
});

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var medium_perc = data.mediumSolved / data.totalMedium * 100
        var medium_count = data.mediumSolved
        $('#mediumcount').append(`<h5>Medium</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-warning\" role=\"progressbar\" aria-valuenow=\"` + String(medium_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(medium_perc) + `%\"></div>` + String(medium_count) + "</div>")
    }
});

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var hard_perc = data.hardSolved / data.totalHard * 100
        var hard_count = data.hardSolved
        $('#hardcount').append(`<h5>Hard</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-danger\" role=\"progressbar\" aria-valuenow=\"` + String(hard_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(hard_perc) + `%\"></div>` + String(hard_count) + "</div>")
    }
});

// $.ajax({
//     type: "GET",
//     cache: false,
//     url: "https://api.github.com/repos/Sadamingh/code-tracker/git/trees/main",
//     headers: {'Authorization': '${{ secrets.TOKEN }}' },
//     dataType: "json",
//     success: function(data) {
//         var arr = data.tree
//         for(var idx in arr) {
//             if(arr[idx].type === "tree") {
//                 let title = "";
//                 let titleArr = arr[idx].path.split("-")
//                 let titleNum = titleArr[0]
//                 titleArr.shift()
//                 for(var titleIdx in titleArr) {
//                     title += titleArr[titleIdx].charAt(0).toUpperCase() + titleArr[titleIdx].slice(1) + " "
//                 }
//                 $('#content').append("<div class=\"col-2\"><span class=\"badge text-bg-primary\">" + titleNum + 
//                  "</span> </div><div class=\"col-8\"> " + title + "</div> <div class=\"col-2\">" + 
//                  "<a href=\"https://github.com/Sadamingh/code-tracker/blob/main/" + 
//                  arr[idx].path + "\">link</a></div>")
//             }
//         }
//     }
// });

$.ajax({
    type: "GET",
    cache: false,
    url: "https://api.github.com/repos/Sadamingh/code-tracker/git/trees/main",
    headers: {'Authorization': '${{ secrets.TOKEN }}' },
    dataType: "json",
    success: function(data) {
        var arr = data.tree;
        for(var idx in arr) {
            if(arr[idx].type === "tree") {
                let title = "";
                let titlePath = arr[idx].path
                let titleArr = arr[idx].path.split("-");
                let titleNum = titleArr[0];
                titleArr.shift();
                for(var titleIdx in titleArr) {
                    title += titleArr[titleIdx].charAt(0).toUpperCase() + titleArr[titleIdx].slice(1) + " ";
                }

                const $row = $('<div>', { class: 'row' });
                $row.append($('<div>', { class: 'col-2' }).append($('<span>', { class: 'badge text-bg-primary' }).text(titleNum)));
                $row.append($('<div>', { class: 'col-9 hoverElement' }).css('position', 'relative').append($('<span>').text(title)));

                const $preElement = $('<pre>', { class: 'content' });
                const $codeElement = $('<code>', { class: 'language-python' });
                const $overlay = $('<div>', { class: 'overlay' });

                $preElement.append($codeElement);
                $row.find('.hoverElement').append($preElement).append($overlay);
                $row.append($('<div>', { class: 'col-1' }).append($('<a>', { href: 'https://github.com/Sadamingh/code-tracker/blob/main/' + arr[idx].path }).text('link')));

                $('#content').append($row);
                $preElement.hide();

                $row.find('span').on('mousedown', function() {
                    $preElement.show();
                    // $overlay.show();
                    const url = 'https://raw.githubusercontent.com/Sadamingh/code-tracker/main/' + titlePath + '/' +  titlePath + '.py'
                    $.get(url, function(data) {
                        $codeElement.text(data);
                        Prism.highlightElement($codeElement[0]);
                    }).fail(function() {
                        $preElement.hide();
                        // $overlay.hide();
                    });
                });

                // $hoverElement.on('mouseleave', function() {
                //     if (!$preElement.is(':hover')) {
                //         $preElement.hide();
                //         // $overlay.hide();
                //     }
                // });

                $preElement.on('mousedown', function() {
                    $preElement.hide();
                    // $overlay.hide();
                });

                $preElement.on('mouseleave', function() {
                    $preElement.hide();
                    // $overlay.hide();
                });
            }
        }
    }
});


$("#click-me").click(function () {

    $.ajax({
        success: function (data) {                               
            console.log(data);   
            $('#info-modal').addClass("show"); 
        },
        async: true
    });    
});
    
$(".modal-dialog .close").click(function(){
    $(this).closest(".modal-dialog").removeClass("show"); 
});