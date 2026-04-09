async function submitData() {
  const n1 = document.getElementById('steps').value;
  const n2 = document.getElementById('delay').value;

  const response = await fetch('/move_stepper', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({steps: n1, delay: n2})
  });

  const data = await response.json();
}

