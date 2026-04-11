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

async function reverseStepper() {
  const response = await fetch('reverse_stepper', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
  });

  const data = await response.json();
}

async function refreshStatus() {
  const statusDiv = document.createElement("div");
  try {
    const response = await fetch('/status');
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    
    const status = await response.json();
    console.log(status)
  } catch (error) {
    console.error(error.message);
  }
}

