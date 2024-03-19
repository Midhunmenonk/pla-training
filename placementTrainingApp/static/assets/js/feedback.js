const feedbackCards = document.querySelectorAll('.feedback-card');

feedbackCards.forEach((card) => {
  const pendingButton = card.querySelector('.pending');
  const doneButton = card.querySelector('.done');

  doneButton.addEventListener('click', () => {
    card.classList.add('done');
    card.classList.remove('pending');
    pendingButton.disabled = true;
    doneButton.disabled = true;
  });

  pendingButton.addEventListener('click', () => {
    card.classList.add('pending');
    card.classList.remove('done');
    pendingButton.disabled = true;
    doneButton.disabled = false;
  });
});