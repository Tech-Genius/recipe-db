$(document).ready(function () {
    $(window).load(function () {

        // will first fade out the loading animation 


        // will fade out the whole DIV that covers the website. 
        $(".ajaxLoader").delay(200).fadeOut("slow");

    })
    // $('.ajaxLoader').hide();
    $(".filter-tag").on('click', function () {
        var _filterObj = {};
        $(".filter-tag").each(function (index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;

            });

        });


        $.ajax({
            url: '/filter-category',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function () {
                $('.ajaxLoader').show();

                $(".ajaxLoader").delay(1200).fadeOut("slow");



            },
            success: function (res) {
                console.log(res)
                $("#product_filtered").html(res.data)

            }
        });

    });
});









// Add to cart
$(document).on('click', "#add_to_cart_btn", function () {
    var _vm = $(this);
    // var _index=_vm.attr('data-index');
    var _qty = $("#productQty").val();
    var _productId = $(".product-id").val();
    var _productImage = $(".product-image").val();
    var _productTitle = $(".product-title").val();
    var _productPrice = $(".product-price").val();

    // Ajax
    $.ajax({
        url: '/add-to-cart',
        data: {
            'id': _productId,
            'image': _productImage,
            'qty': _qty,
            'title': _productTitle,
            'price': _productPrice,
        },
        dataType: 'json',
        beforeSend: function () {
            _vm.attr('disabled', true);
        },
        success: function (res) {
            $(".cart_item_total").text(res.totalitems)

            _vm.attr('disabled', false);
        }
    });
    // End
});


// Delete item from cart
$(document).on('click', '#delete-item', function () {
    var _pId = $(this).attr('data-item');
    var _vm = $(this);
    // Ajax
    $.ajax({
        url: '/delete-from-cart',
        data: {
            'id': _pId,
        },
        dataType: 'json',
        beforeSend: function () {
            _vm.attr('disabled', true);
        },
        success: function (res) {
            $(".cart_item_total").text(res.totalitems);
            _vm.attr('disabled', false);
            $("#cartList").html(res.data);
        }
    });
    // End
});


// Update cart
$(document).on('click', '#update-item', function () {
    var _pId=$(this).attr('data-item');
    var _pQty=$(".product-qty-"+_pId).val();
    var _vm=$(this);
    // Ajax
    $.ajax({
        url: '/update-cart',
        data: {
            'id':_pId,
            'qty':_pQty
        },
        dataType: 'json',
        beforeSend: function () {
            _vm.attr('disabled', true);
        },
        success: function (res) {
            // $(".cart_item_total").text(res.totalitems);
            _vm.attr('disabled', false);
            $("#cartList").html(res.data);
        }
    });
    // End
});

