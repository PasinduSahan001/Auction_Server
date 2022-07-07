// $(document).ready(function() {

//     $('form').on('submit', function(event) {

//         $.ajax({
//                 data: {
//                     name: $('#nameInput').val(),

//                 },
//                 type: 'POST',
//                 url: '/process'
//             })
//             .done(function(data) {

//                 if (data.error) {
//                     $('#errorAlert').text(data.error).show();
//                     $('#successAlert').hide();
//                 } else {
//                     $('#successAlert').text(data.name).show();
//                     $('#errorAlert').hide();
//                 }

//             });

//         event.preventDefault();

//     });

// });

// $(document).ready(function() {

//     function loadloop() {

//         $.ajax({
//                 data: {
//                     name: $('#nameInput').val(),

//                 },
//                 type: 'POST',
//                 url: '/process'
//             })
//             .done(function(data) {

//                 if (data.error) {
//                     $('#errorAlert').text(data.error).show();
//                     $('#successAlert').hide();
//                 } else {
//                     $('#successAlert').text(data.name).show();
//                     $('#errorAlert').hide();
//                 }

//             });

//     }

//     loadloop()


// });


// function loadloop() {

//     setInterval(function() {
//         $.ajax({
//                 data: {
//                     name: "Notification"

//                 },
//                 type: 'POST',
//                 url: '/process'
//             })
//             .done(function(data) {

//                 if (data.error) {
//                     $('#errorAlert').text(data.error).show();
//                     $('#successAlert').hide();
//                 } else {
//                     //$('#successAlert').text(data.name).show();
//                     $('#errorAlert').hide();
//                     //window.alert(data.Title, data.Base_price);
//                     $('#successAlert').text(data.Title, data.Base_Price, data.Max_bid).show();
//                     console.log(data.Title, data.Base_Price, data.Max_bid)
//                     alert(data.Title, data.Base_Price);
//                     //$("#myModal").modal();
//                 }

//             });

//     }, 5000);
//     $('#successAlert').hide();

// }

// loadloop()



// function loadloop() {

//     $.ajax({
//             data: {
//                 name: "Notification"

//             },
//             type: 'POST',
//             url: '/process'
//         })
//         .done(function(data) {


//             setInterval(function() {


//                 if (data.error) {
//                     $('#errorAlert').text(data.error).show();
//                     $('#successAlert').hide();
//                 } else {
//                     $('#successAlert').text(data.name).show();
//                     $('#errorAlert').hide();
//                     //window.alert(data.Title, data.Base_price);
//                     console.log(data.Title, data.Base_Price, data.Max_bid)
//                     $('#successAlert').text(data.Title, data.Base_Price, data.Max_bid).show();
//                     //                  $('#errorAlert').hide();
//                 }

//             }, 5000);

//         });

// }

// loadloop()

// function loadloop() {

//     $.ajax({
//             data: {
//                 name: "Notification"

//             },
//             type: 'POST',
//             url: '/process'
//         })
//         .done(function(data) {





//             if (data.error) {
//                 $('#errorAlert').text(data.error).show();
//                 $('#successAlert').hide();
//             } else {
//                 $('#successAlert').text(data.name).show();
//                 $('#errorAlert').hide();
//                 //window.alert(data.Title, data.Base_price);
//                 console.log(data.Title, data.Base_Price, data.Max_bid)
//                 $('#successAlert').text(data.Title, data.Base_Price, data.Max_bid).show();
//                 //                  $('#errorAlert').hide();
//             }



//         });

// }

// loadloop()



// function loadloop() {

//     setInterval(function() {
//         $.ajax({
//                 data: {
//                     name: "Notification"

//                 },
//                 type: 'POST',
//                 url: '/process'
//             })
//             .done(function(data) {

//                 if (data.error) {
//                     $('#errorAlert').text(data.error).show();
//                     $('#successAlert').hide();
//                 } else {
//                     //$('#successAlert').text(data.name).show();
//                     $('#errorAlert').hide();
//                     //window.alert(data.Title, data.Base_price);
//                     $('#successAlert').text(data.Title, data.Base_Price, data.Max_bid).show();
//                     console.log(data.Title, data.Base_Price, data.Max_bid)
//                         //alert(data.Title, data.Base_Price);
//                         //$("#myModal").modal();

//                     $(function() {
//                         $("#dialog-message").dialog({
//                             modal: true,
//                             buttons: {
//                                 Ok: function() {
//                                     $(this).dialog("close");
//                                 }
//                             }
//                         });
//                     });
//                 }

//             });

//     }, 5000);
//     $('#successAlert').hide();

// }

// loadloop()

function loadloop() {

    setInterval(function() {
        $.ajax({
                data: {
                    name: "Notification"

                },
                type: 'POST',
                url: '/process'
            })
            .done(function(data) {

                if (data.error) {
                    //$('#errorAlert').text(data.error).show();
                    //$('#successAlert').hide();
                    console.log(data.error)
                } else {
                    if (data.Type == "New_Bid") {
                        //$('#successAlert').text(data.name).show();
                        //$('#errorAlert').hide();
                        //window.alert(data.Title, data.Base_price);
                        $('#successAlert').text("New Bid For " + data.Title + ". New BID Price Is Rs " + data.Max_bid + "/=").show();
                        console.log(data.Title, data.Base_Price, data.Max_bid);
                        //alert(data.Title, data.Base_Price);
                        //$("#myModal").modal();
                    }

                    if (data.Type == "New_Item") {
                        //$('#successAlert').text(data.name).show();
                        //$('#errorAlert').hide();
                        //window.alert(data.Title, data.Base_price);
                        $('#successAlert').text("New Item add. " + data.Title + ". Base price Is Rs " + data.Base_Price + "/=" + " Bid expiry_on" + " " + data.Expiry_Date).show();
                        console.log(data.Title, data.Base_Price, data.Expiry_Date);
                        //alert(data.Title, data.Base_Price);
                        //$("#myModal").modal();
                    }

                    $(function() {
                        $("#dialog-message").dialog({
                            modal: true,
                            buttons: {
                                Ok: function() {
                                    $(this).dialog("close");
                                    data.Title = "LOL"
                                    $('#successAlert').hide();

                                    $.ajax({
                                        data: {
                                            name: "Notification_OFF"

                                        },
                                        type: 'POST',
                                        url: '/process'
                                    })
                                }
                            }
                        });
                    });
                }

            });

    }, 1000);
}

loadloop()