$(function () {
	$('.cabinet-page .cabinet-content .news .archive a').click(function () {
		$(this).toggleClass('active');
		$(this).next('ul').toggle();
	});
	$('.cabinet-page .cabinet-content .ballanse .history .select a').click(function () {
		$(this).toggleClass('active');
		$(this).next('ul').toggle();
	});
	$('.cabinet-page .cabinet-content .ballanse .top-info .select a').click(function () {
		$(this).toggleClass('active');
		$(this).next('ul').toggle();
	});
	$('.header .langs-block .lang, .header .langs-block .window').hover(
		function () {
			$('.header .langs-block .window').show();
		}, function () {
			$('.header .langs-block .window').hide();
		}
	);
	$('.top-link button').click(function () {
		$('.top-link .top-link__window').toggleClass('visible');
	});
	$('.popup .window .close').click(function () {
		$('.popup').fadeOut();
	});
	$('.header .name div img').click(function () {
		$('.popup.popup--avatar').fadeIn();
	});
	$('.item__btn--popup-ip').click(function () {
		$('.popup.popup--ip').fadeIn();
	});
	$('.item__btn--password-activation').click(function () {
		$('.popup.popup--password-activation').fadeIn();
	});
	$('.item__btn--sms-activation').click(function () {
		$('.popup.popup--sms-activation').fadeIn();
	});
	$('.choosing-specialty__specialties-add, .personal__specialty-notfound, .personal__skills-btn, .select-specialty').click(function (event) {
		event.preventDefault();
		$('.popup.popup--add-specialty').fadeIn();
	});
	$('.header .logo .menu-button').click(function () {
		$('.header .logo ul').toggle();
	});

	$(".personal__employee-add").off().on("click", function () {
		var newItemHTML = `
        <div class="personal__employee-item new-item">
            <input class="personal__employee-input" type="text" placeholder="Фамилия и имя сотрудника">
        </div>
    `;
		$(newItemHTML).appendTo(".personal__employee-items").find(".personal__employee-input").val("");
	});

	$('.item__edit-password').click(function () {
		$(this).closest('.item').toggleClass('active');
	});


	var $countyToggle = $('.county-toggle, .task-detail__contry-arrow');
	var $countyDropdown = $('.county-dropdown');

	$countyToggle.on('click', function () {
		event.preventDefault();
		$countyDropdown.toggleClass('active');
	});

	$(document).on('click', function (event) {
		if (!$(event.target).closest('.county-toggle, .task-detail__contry-arrow, .county-dropdown').length) {
			$countyDropdown.removeClass('active');
		}
	});

	$('.county-dropdown__item input[type="checkbox"]').change(function () {
		const imageSrc = $(this).siblings('img').attr('src');
		const countryName = $(this).siblings('p').text();
		if ($(this).is(':checked')) {
			const newListItem = $('<div class="county-list__item" title="' + countryName + '"><img src="' + imageSrc + '"></div>');
			$('.county-list').append(newListItem);
		} else {
			$('.county-list__item').has('img[src="' + imageSrc + '"]').remove();
		}
	});

	$('.choosing-specialty__area-btn').on('click', function () {
		$('.choosing-specialty__area-btn').removeClass('active');
		$('.choosing-specialty__specialties-btn').removeClass('active');
		$('.choosing-specialty__category-btn').removeClass('active');
		$(this).addClass('active');
		$('.choosing-specialty__category').addClass('visible');
		$('.choosing-specialty__specialties').removeClass('visible');
	});
	$('.choosing-specialty__category-btn').on('click', function () {
		$('.choosing-specialty__category-btn').removeClass('active');
		$(this).addClass('active');
		$('.choosing-specialty__specialties').addClass('visible');
		$('.choosing-specialty__specialties-btn').removeClass('active');
	});




	$(document).on('click', '.choosing-specialty__specialties-btn', function () {
		var specialtyText = $(this).text();
		var selectedItem = $('.choosing-specialty__selected-item').filter(function () {
			return $(this).find('p').text() === specialtyText;
		});

		if (selectedItem.length > 0) {
			selectedItem.remove();
			$(this).removeClass('active');
		} else {
			var checkbox = $('<input type="checkbox" checked>');
			var span = $('<span></span>');
			var paragraph = $('<p></p>').text(specialtyText);
			selectedItem = $('<label class="choosing-specialty__selected-item"></label>');

			selectedItem.append(checkbox);
			selectedItem.append(span);
			selectedItem.append(paragraph);

			$('.choosing-specialty__selected-title').after(selectedItem);
			$(this).addClass('active');
		}
	});

	$(document).on('click', '.choosing-specialty__selected-item input[type="checkbox"]', function () {
		$(this).parent('.choosing-specialty__selected-item').remove();
		var specialtyText = $(this).siblings('p').text();
		$('.choosing-specialty__specialties-btn').filter(function () {
			return $(this).text() === specialtyText;
		}).removeClass('active');
	});

	$('.select-specialty__item-delete').on('click', function (event) {
		event.preventDefault();
		$(this).closest('.select-specialty__item').remove();
	});


	$('.filter__box-btn').click(function () {
		var $button = $(this);
		var $filter = $('.orders-page .filter form');

		if ($button.text() === 'Развернуть') {
			$button.text('Свернуть');
			$filter.addClass('visible');
		} else {
			$button.text('Развернуть');
			$filter.removeClass('visible');
		}
	});



	$('.add-specialty__textarea').on('input', function () {
		var maxLength = 255;
		var currentLength = $(this).val().length;
		var remainingLength = maxLength - currentLength;
		$('.add-specialty__num').text(currentLength + ' / ' + maxLength);
		if (remainingLength < 0) {
			var trimmedText = $(this).val().substring(0, maxLength);
			$(this).val(trimmedText);
			$('.add-specialty__num').text(maxLength + ' / ' + maxLength);
		}
	});

	$('.task-create__form-input').on('input', function () {
		var maxLength = 100;
		var currentLength = $(this).val().length;
		var remainingLength = maxLength - currentLength;
		$('.task-create__box.title .task-create__form-num').text(currentLength + ' / ' + maxLength);
		if (remainingLength < 0) {
			var trimmedText = $(this).val().substring(0, maxLength);
			$(this).val(trimmedText);
			$('.task-create__box.title .task-create__form-num').text(maxLength + ' / ' + maxLength);
		}
	});

	$('.task-create__form-textarea').on('input', function () {
		var maxLength = 5000;
		var currentLength = $(this).val().length;
		var remainingLength = maxLength - currentLength;
		$('.task-create__box.descr .task-create__form-num').text(currentLength + ' / ' + maxLength);
		if (remainingLength < 0) {
			var trimmedText = $(this).val().substring(0, maxLength);
			$(this).val(trimmedText);
			$('.task-create__box.descr .task-create__form-num').text(maxLength + ' / ' + maxLength);
		}
	});

	$('.cabinet-page .cabinet-content .chat .comment textarea').on('input', function () {
		var maxLength = 1000;
		var currentLength = $(this).val().length;
		var remainingLength = maxLength - currentLength;
		$('.cabinet-page .cabinet-content .chat .comment .num').text(currentLength + ' / ' + maxLength);
		if (remainingLength < 0) {
			var trimmedText = $(this).val().substring(0, maxLength);
			$(this).val(trimmedText);
			$('.cabinet-page .cabinet-content .chat .comment .num').text(maxLength + ' / ' + maxLength);
		}
	});



	$('#portfolio-container').on('change', '.task-feedback__portfolio-label input', function () {
		var input = $(this);
		var file = input[0].files[0];
		if (file) {
			var reader = new FileReader();
			reader.onload = function (e) {
				var img = $('<img>').attr('src', e.target.result);
				var portfolioItem = input.closest('.task-feedback__portfolio-item');
				var imageContainer = portfolioItem.find('.task-feedback__portfolio-image');
				imageContainer.empty();
				imageContainer.append(img);
				portfolioItem.addClass('active');
			};
			reader.readAsDataURL(file);
		}
	});
	$('.task-feedback__portfolio-label input').each(function () {
		var input = $(this);
		var portfolioItem = input.closest('.task-feedback__portfolio-item');

		if (input[0].files && input[0].files[0]) {
			portfolioItem.addClass('active');
		}
	});



	var counter = 4;
	$(".task-feedback__portfolio-add").click(function () {
		for (var i = 0; i < 3; i++) {
			var itemId = "file-desktop-" + counter;
			var newItem = '<div class="task-feedback__portfolio-item">' +
				'<div class="task-feedback__portfolio-image"></div>' +
				'<div class="task-feedback__portfolio-box">' +
				'<button class="task-feedback__portfolio-btn">Загрузить из Портфолио</button>' +
				'<label class="task-feedback__portfolio-label" for="' + itemId + '">' +
				'<input type="file" id="' + itemId + '">' +
				'<span>Загрузить из комьютера</span>' +
				'</label>' +
				'</div>' +
				'</div>';

			$(".task-feedback__portfolio-items").append(newItem);
			counter++;
		}
		return false;
	});


	$(".task-feedback__portfolio-add--contest").click(function () {
		for (var i = 0; i < 3; i++) {
			var itemId = "file-desktop-" + counter;
			var newItem = '<div class="task-feedback__portfolio-item">' +
				'<div class="task-feedback__portfolio-image"></div>' +
				'<div class="task-feedback__portfolio-box">' +
				'<label class="task-feedback__portfolio-label" for="' + itemId + '">' +
				'<input type="file" id="' + itemId + '">' +
				'<span>Загрузить</span>' +
				'</label>' +
				'</div>' +
				'</div>';

			$(".task-feedback__portfolio-items").append(newItem);
			counter++;
		}
		return false;
	});


	$('.task-feedback__btn').on('click', function () {
		$(this).addClass('hidden');
		$('.task-feedback__inner').addClass('visible');
	});
	$('.task-feedback__cancellation').on('click', function () {
		$('.task-feedback__btn').removeClass('hidden');
		$('.task-feedback__inner').removeClass('visible');
	});



	$('.task-list__item-messagebtn').on('click', function (event) {
		event.preventDefault();
		var messageBtn = $(this);
		var messageForm = messageBtn.closest('.task-list__item-form');
		var messageBox = messageForm.find('.task-list__item-message');

		messageBox.toggleClass('visible');
	});


	function adjustTextarea(textarea) {
		textarea.style.height = "auto";
		textarea.style.height = (textarea.scrollHeight) + "px";
	}

	var textareas = document.querySelectorAll(".task-selected__send-textarea");
	for (var i = 0; i < textareas.length; i++) {
		textareas[i].addEventListener("input", function () {
			adjustTextarea(this);
		}, false);
		adjustTextarea(textareas[i]);
	}

	$('.task-selected__information').on('click', function () {
		$(this).toggleClass('hidden-img');
		$(this).closest('.task').toggleClass('task--hidden')
	});


	// $('input[name="task-country"]').on('change', function () {
	// 	if ($(this).is(':checked')) {
	// 		var country = $(this).closest('label').find('p').text();
	// 		$('.task-detail__contry-text').text(country);
	// 	}
	// });


	$(document).ready(function () {
		var maxSize = 100;
		var maxFiles = 10;
		var totalSize = 0;
		var numFiles = 0;

		$('#task-file-input').on('change', function () {

			var files = this.files;
			var numSelected = files.length;

			if (numSelected > maxFiles) {
				alert('Вы выбрали слишком много файлов. Пожалуйста, выберите не более ' + maxFiles + ' файлов.');
				this.value = '';
				return;
			}

			for (var i = 0; i < numSelected; i++) {
				var file = files[i];
				var fileSize = (file.size / 1024 / 1024).toFixed(2);
				totalSize += parseFloat(fileSize);

				if (totalSize > maxSize) {
					alert('Общий размер выбранных файлов превышает ' + maxSize + ' МБ. Пожалуйста, выберите файлы с меньшим размером.');
					this.value = '';
					totalSize = 0;
					numFiles = 0;
					return;
				}

				numFiles++;
				var item = $('<div class="task-create__files-item"><img src="img/task-file.svg" alt=""><span>' + fileSize + 'МБ</span></div>');
				$('.task-create__files-list').append(item);
			}

			$('.task-create__files-num').text('Итого загружено ' + numFiles + ' файлов ' + totalSize.toFixed(2) + 'МБ');
		});
		$('.task-create__files-btn').on('click', function (event) {
			event.preventDefault();
			$('#task-file-input').click();
		});
	});


	$('.item__contests-toggle').on('click', function () {
		$(this).closest('.item').toggleClass('contests-active');
	});


	$('.freelancers__specialties-more').on('click', function () {
		var specialtiesBtn = $(this);
		var specialtiesInner = specialtiesBtn.closest('.freelancers__item-specialties');
		var specialtiesItems = specialtiesInner.find('.freelancers__specialties-items');

		specialtiesItems.toggleClass('visible');
	});



	$('.footer-security').on('click', function (event) {
		event.preventDefault();
		$('.footer-security__buttons').toggleClass('visible');
	});


	$('.ticket__box-btn').on('click', function () {
		var ticketBtn = $(this);
		var ticketItem = ticketBtn.closest('.cabinet-page .cabinet-content .ticket .links ul li');
		var ticketBox = ticketItem.find('.ticket__box');

		ticketBox.slideToggle(300);
	});


	$('.ticket__btn').on('click', function () {
		var ticketBtn = $(this);
		var ticketItem = ticketBtn.closest('.ticket__item');
		var ticketText = ticketItem.find('.ticket__text');

		ticketText.slideToggle(300);
	});


	$('.cabinet-page .cabinet-content .ballanse .top-info .select ul li button, .cabinet-page .cabinet-content .news .archive ul li button').on('click', function () {
		$('.period__dropdown').toggle();
	});


	$("#period-from").change(function () {
		var fromDate = $(this).val();
		$(".period-from").text(fromDate);
	});
	$("#period-to").change(function () {
		var toDate = $(this).val();
		$(".period-to").text(toDate);
	});



	document.querySelectorAll('.personal__input-eye').forEach((item) => {
		item.addEventListener('click', function () {
			this.classList.toggle('no-eye');
		});
	});
	var bool = true;
	document.querySelectorAll('.personal__input.input-password').forEach((item) => {
		itemIcon = document.querySelectorAll('.personal__input-eye');
		item.addEventListener('click', (e) => {
			if (bool) {
				bool = false;
				item.parentNode.querySelector('input').setAttribute('type', 'text');

			} else {
				bool = true;
				item.parentNode.querySelector('input').setAttribute('type', 'password');
			}
		});
	});


	$('.faq__theme-toggle').on('click', function () {
		$(this).closest('.faq__theme').find('.faq__theme-dropdown').toggle();
	});
	$('.faq__theme-link').on('click', function (event) {
		event.preventDefault();
		$(this).closest('.faq__theme-dropdown').toggle();
	});


	$('.faq__accordion-toggle').on('click', function () {
		var accordionBtn = $(this);
		var accordionItem = accordionBtn.closest('.faq__accordion');
		var accordiontext = accordionItem.find('.faq__accordion-text');

		accordionBtn.toggleClass('active');
		accordiontext.slideToggle(300);
	});


	$('button[data-first]').click(function () {
		var firstValue = $(this).data('first');

		var firstBlock = $('div[data-first="' + firstValue + '"]');
		var position = firstBlock.offset().top;

		$('html, body').animate({ scrollTop: position - 80 }, 'slow');

		$('button[data-first]').removeClass('active');
		$(this).addClass('active');
	});

	$('button[data-referal]').click(function () {
		var firstValue = $(this).data('referal');

		var firstBlock = $('div[data-referal="' + firstValue + '"]');
		var position = firstBlock.offset().top;

		$('html, body').animate({ scrollTop: position - 80 }, 'slow');

		$('button[data-referal]').removeClass('active');
		$(this).addClass('active');
	});




	$(document).ready(function () {
		var oldText = $('.first__title').text();
		$('.first__block').each(function () {
			var block = $(this);
			var blockIndex = block.data('first');
			$(window).scroll(function () {
				var scrollTop = $(window).scrollTop();
				var blockTop = block.offset().top - 85;

				if (scrollTop >= blockTop) {
					var headingText = block.find('h3:first').text();
					block.data('heading', headingText);
					block.data('top', blockTop);
				}
			});
		});
		$(window).scroll(function () {
			var scrollTop = $(window).scrollTop();
			var currentBlock = null;
			var isVisible = false;
			$('.first__block').each(function () {
				var blockTop = $(this).data('top');
				var blockBottom = blockTop + $(this).outerHeight();
				var blockIndex = $(this).data('first');

				if (scrollTop >= blockTop && scrollTop <= blockBottom) {
					currentBlock = $(this);
					isVisible = true;
					return false;
				}
			});
			if (currentBlock) {
				var headingText = currentBlock.data('heading');
				$('.first__title').text(headingText);
			} else {
				$('.first__title').text(oldText);
			}
		});
	});




	$('.first__accordion-toggle').on('click', function () {
		$(this).closest('.first__accordion').find('.first__accordion-text').slideToggle(300);
	});



	$('.header .user .play, .header .user .round, .header .user i').on('click', function (event) {
		event.preventDefault();
		$('.user').toggleClass('vacation');
		$('.user').toggleClass('busy');
	});



	$('.ticket .create').on('click', function () {
		$('.ticket form').attr('style', 'display: block;');
		$('.ticket form')[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
	});

	$('.faq__public').on('click', function (event) {
		event.preventDefault();
		$('.faq-public')[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
	});

	$('.top-link button').on('click', function () {
		var button = $(this);
		var links = $(this).closest('.ticket').find('.links');

		links.slideToggle();

		if (button.text() === 'Свернуть ответы') {
			button.text('Часто задаваемые вопросы в Тикет-системе');
		} else {
			button.text('Свернуть ответы');
		}
	});


	$('.period__dropdown-dtn').on('click', function () {
		$('.archive ul, period__dropdown').toggle();
		$(this).closest('.select ul').toggle();
	});



	$(document).ready(function () {
		var tooltips = [
			{ id: "tooltip1", text: "Ссылка скопирована" },
		];

		var tooltipTimeout;

		$('[data-tooltip]').click(function () {
			clearTimeout(tooltipTimeout);

			var tooltipId = $(this).data('tooltip');
			var tooltipText = "";

			for (var i = 0; i < tooltips.length; i++) {
				if (tooltips[i].id === tooltipId) {
					tooltipText = tooltips[i].text;
					break;
				}
			}

			if ($('.tooltip').length === 0) {
				$('body').append('<span class="tooltip">' + tooltipText + '</span>');
			} else {
				$('.tooltip').text(tooltipText);
			}

			var buttonPosition = $(this).offset();
			var buttonWidth = $(this).outerWidth();
			var buttonHeight = $(this).outerHeight();
			var tooltip = $('.tooltip');
			var tooltipWidth = tooltip.outerWidth();
			var tooltipHeight = tooltip.outerHeight();
			var tooltipTop = buttonPosition.top - buttonHeight + 4;
			var tooltipLeft = buttonPosition.left + buttonWidth / 2 - tooltipWidth / 2;

			tooltip.css({
				top: tooltipTop,
				left: tooltipLeft,
				opacity: 1,
				transform: 'translateY(-8px)',
				transition: '0.3s'
			});
		});

		$('[data-tooltip]').mouseleave(function () {
			var tooltip = $('.tooltip');
			tooltip.css({
				opacity: 0,
				transform: 'translateY(0)',
			});

			tooltipTimeout = setTimeout(function () {
				tooltip.remove();
			}, 300);
		});
	});


	$('.copy-link').on('click', function () {
		var text = $(this).prev('.copy-input').text().trim();
		copyTextToClipboard(text);
	});
	function copyTextToClipboard(text) {
		var $tempTextarea = $('<textarea>');
		$tempTextarea.text(text);
		$('body').append($tempTextarea);
		$tempTextarea.select();
		try {
			document.execCommand('copy');
		} catch (err) {
			// Обработка ошибки (если необходимо)
		}
		$tempTextarea.remove();
	}


	$('.period__dropdown-dtn.delete').on('click', function () {
		$('.period__dropdown-input').val('');
		$('.period-from, .period-to').text('...');
	});



	$('.task-detail__info-toggle').on('click', function () {
		$('.task-detail__info-dropdown').toggle();
	});


	$(document).on('click', function (event) {
		var $target = $(event.target);
		if (!$target.closest('.task-menu').length) {
			$('.dropdown').hide();
		}
	});
	$('.task-menu a').on('click', function (event) {
		event.preventDefault();
		var $dropdown = $(this).closest('.task-menu').find('.dropdown');
		$('.dropdown').not($dropdown).hide();
		$dropdown.toggle();
	});


	$('.money-income__way-toggle').on('click', function () {
		$(this).toggleClass('active');
		$('.money-income__way-dropdown').toggle();
	});
	$('.money-income__way-btn').click(function () {
		$('.money-income__way-dropdown').toggle();
		$('.money-income__way-btn').removeClass('active');
		$(this).addClass('active');
		var buttonText = $(this).text();
		$(this).closest('.money-income__way').find('.money-income__way-toggle > span').text(buttonText);
	});

	$('.money-income__details-toggle').on('click', function () {
		$(this).toggleClass('active');
		$(this).closest('.money-income__way-header').toggleClass('active');
		$('.money-income__details-text').toggle();
	});


	$('.job-toggle').on('click', function (event) {
		event.preventDefault();
		var toggleId = $(this).data('toggle');
		var content = $('div.job-toggle-content[data-toggle="' + toggleId + '"]');
		$(this).toggle();
		content.toggle();
	});


	$('.input-password').on('input', function () {
		var password = $(this).val();

		if (password.length >= 8) {
			$('.personal__password-item:nth-child(1)').addClass('checked').removeClass('warning');
		} else {
			$('.personal__password-item:nth-child(1)').removeClass('checked').addClass('warning');
		}

		if (/[a-z]/.test(password) && /[A-Z]/.test(password)) {
			$('.personal__password-item:nth-child(2)').addClass('checked').removeClass('warning');
		} else {
			$('.personal__password-item:nth-child(2)').removeClass('checked').addClass('warning');
		}

		if (/\d/.test(password)) {
			$('.personal__password-item:nth-child(3)').addClass('checked').removeClass('warning');
		} else {
			$('.personal__password-item:nth-child(3)').removeClass('checked').addClass('warning');
		}

		if (/[!@#$%^&*()_+\-=;,./?[\]{}]/.test(password)) {
			$('.personal__password-item:nth-child(4)').addClass('checked').removeClass('warning');
		} else {
			$('.personal__password-item:nth-child(4)').removeClass('checked').addClass('warning');
		}

		var allChecked = $('.personal__password-item').length === $('.personal__password-item.checked').length;

		if (allChecked) {
			$('.personal__submit').removeAttr('disabled');
		} else {
			$('.personal__submit').attr('disabled', 'disabled');
		}
	});

});