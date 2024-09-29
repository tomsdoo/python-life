const IMAGE_REPO = "python-life";
const IMAGE_TAG = "v1.0.0";

(async () => {
  const { exec: originalExec } = await import("node:child_process");
  const { promisify } = await import("node:util");
  const exec = promisify(originalExec);

  async function dockerImageLs() {
    const { stdout } = await exec(`docker image ls --format '{{json .}}'`);
    return stdout
      .split("\n")
      .filter(Boolean)
      .map(line => JSON.parse(line));
  }
  const dockerImages = await dockerImageLs();

  const image = dockerImages.find(
    ({ Repository, Tag }) => Repository === IMAGE_REPO && Tag === IMAGE_TAG
  );
  if(image != null) {
    console.log(
      await exec(`docker image rm ${image.ID}`)
        .then(({ stdout, stderr }) => [stdout, stderr].join("\n"))
    );
  }
  
  console.log(
    await exec(`docker image build -f Dockerfile -t ${IMAGE_REPO}:${IMAGE_TAG} .`)
      .then(({stdout, stderr}) => [stdout,stderr].join("\n"))
  );
    
})().finally(() => process.exit());



