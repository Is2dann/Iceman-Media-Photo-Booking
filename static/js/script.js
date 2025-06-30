function toggleEditForm(commentId) {
    const form = document.getElementById(`edit-form-${commentId}`);
    if (form.style.display === "none") {
        form.style.display = "block";
    } else {
        form.style.display = "none";
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const deleteModal = document.getElementById('deleteModal');
    deleteModal.addEventListener('show.bs.modal', function (event) {
        let button = event.relatedTarget;
        let commentId = button.getAttribute('data-comment-id');
        let commentText = button.getAttribute('data-comment-text');

        let deleteForm = document.getElementById('deleteCommentForm');
        let commentDisplay = document.getElementById('commentToDeleteText');

        deleteForm.action = `/portfolio/comment/delete/${commentId}/`;
        commentDisplay.textContent = commentText;
    });
});

document.addEventListener('DOMContentLoaded', function () {
// DELETE modal already handled before

const editModal = document.getElementById('editModal');
editModal.addEventListener('show.bs.modal', function (event) {
    let button = event.relatedTarget;
    let commentId = button.getAttribute('data-comment-id');
    let commentText = button.getAttribute('data-comment-text');

    let editForm = document.getElementById('editCommentForm');
    let textarea = document.getElementById('editCommentTextarea');

    // Update action and content
    editForm.action = `/portfolio/comment/edit/${commentId}/`;
    textarea.value = commentText;
    });
});