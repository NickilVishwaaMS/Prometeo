document.getElementById('upload-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-result').innerText = 'Prediction: ' + data.prediction;
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('upload-form').addEventListener('change', function(event) {
    var fileInput = event.target;
    var file = fileInput.files[0];
    
    if (file && file.type.match('image.*')) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var previewImage = document.getElementById('image-preview');
            previewImage.src = e.target.result;

            // Make the image container and preview image visible and centered
            var imageContainer = document.getElementById('image-container');
            imageContainer.style.display = 'flex'; // Display the container with flex
            previewImage.style.maxWidth = 'auto';  // Remove restrictions on image size
            previewImage.style.maxHeight = 'auto'; // Use auto to maintain aspect ratio
        };
        reader.readAsDataURL(file);
    }
});
