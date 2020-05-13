<template>
  <div class="FileUpload">
    <VueFileAgent
      ref="vueFileAgent"
      :theme="'list'"
      :multiple="true"
      :deletable="true"
      :meta="true"
      :accept="'.pdf,.docx'"
      :maxSize="'2MB'"
      :maxFiles="10"
      :helpText="'Choose .pdf or .docx files'"
      :errorText="{
    type: 'Invalid file type. Only .pdf or .docx allowed',
    size: 'Files should not exceed 2MB in size',
    }"
      @select="filesSelected($event)"
      @beforedelete="onBeforeDelete($event)"
      @delete="fileDeleted($event)"
      v-model="fileRecords"
    />
    <button
      :disabled="!fileRecordsForUpload.length"
      @click="uploadFiles()"
    >Upload {{ fileRecordsForUpload.length }} files</button>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
  data() {
    return {
      fileRecords: [],
      uploadUrl: "http://127.0.0.1:5000/upload",
      uploadHeaders: { "X-Test-Header": "vue-file-agent" },
      fileRecordsForUpload: []
    };
  },
  methods: {
    uploadFiles() {
      // Using the default uploader. You may use another uploader instead.
      this.$refs.vueFileAgent.upload(
        this.uploadUrl,
        this.uploadHeaders,
        this.fileRecordsForUpload
      );
      this.fileRecordsForUpload = [];
    },
    deleteUploadedFile(fileRecord) {
      // Using the default uploader. You may use another uploader instead.
      this.$refs.vueFileAgent.deleteUpload(
        this.uploadUrl,
        this.uploadHeaders,
        fileRecord
      );
    },
    filesSelected(fileRecordsNewlySelected) {
      var validFileRecords = fileRecordsNewlySelected.filter(
        fileRecord => !fileRecord.error
      );
      this.fileRecordsForUpload = this.fileRecordsForUpload.concat(
        validFileRecords
      );
    },
    onBeforeDelete(fileRecord) {
      var i = this.fileRecordsForUpload.indexOf(fileRecord);
      if (i !== -1) {
        this.fileRecordsForUpload.splice(i, 1);
      } else {
        // if (confirm("Are you sure you want to delete?")) {
        this.$refs.vueFileAgent.deleteFileRecord(fileRecord); // will trigger 'delete' event
        // }
      }
    },
    fileDeleted(fileRecord) {
      var i = this.fileRecordsForUpload.indexOf(fileRecord);
      if (i !== -1) {
        this.fileRecordsForUpload.splice(i, 1);
      } else {
        this.deleteUploadedFile(fileRecord);
      }
    }
  }
};
</script>

