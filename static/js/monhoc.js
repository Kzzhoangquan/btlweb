document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const subjectList = document.getElementById('subject-list');

    searchInput.addEventListener('input', function() {
        const keyword = this.value.trim();
        if (keyword === '') {
            subjectList.style.display = 'none';
            return;
        }

        fetch(`/search_subjects?keyword=${keyword}`)
            .then(response => response.json())
            .then(data => {
                displaySubjects(data.subjects);
            });
    });

    function displaySubjects(subjects) {
        subjectList.innerHTML = '';
        if (subjects.length === 0) {
            subjectList.style.display = 'none';
            return;
        }

        subjects.forEach(subject => {
            const li = document.createElement('li');
            li.textContent = subject;
            li.addEventListener('click', function() {
                searchInput.value = subject;
                subjectList.style.display = 'none';
            });
            subjectList.appendChild(li);
        });

        subjectList.style.display = 'block';
    }
});
